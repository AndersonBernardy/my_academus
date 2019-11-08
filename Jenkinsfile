pipeline {
  agent any
  options {
    // Stop build if a step fail
    skipStagesAfterUnstable()
    // Only keep the 10 most recent builds
    buildDiscarder(logRotator(numToKeepStr:'10'))
  }
  environment {
    BASE_IMAGE = 'django-mariadb-base'
    TESTER_IMAGE = 'django-selenium-tester'
    APP_IMAGE = 'my-academus-app'
    APP_TESTER_IMAGE = 'my-academus-tester'
  }

  stages {
    stage('Setup') {
      stages {
        stage('Setup Base Image') {
          steps {
            script {
              def image = sh "docker images -q ${BASE_IMAGE}"
              if (image == ''){
                sh "echo 'Building Image: ${BASE_IMAGE}'"
                docker.build "${BASE_IMAGE}"
              } else {
                sh "echo 'Image already built: ${BASE_IMAGE}'"
              }
            }
          }
        }
        stage('Setup Base Tester Image') {
          script {
            def image = sh "docker images -q ${TESTER_IMAGE}"
            if (image == ''){
              sh "echo 'Building Image: ${TESTER_IMAGE}'"
              docker.build "${TESTER_IMAGE}"
            } else {
              sh "echo 'Image already built: ${TESTER_IMAGE}'"
            }
          }
        }
      }
    }

    stage('Test') {
      stages {
        stage('Build Tester Image') {
          steps {
            script {
              sh "echo 'Building Image: ${APP_TESTER_IMAGE}:${env.BUILD_ID}'"
              docker.build "${APP_TESTER_IMAGE}:${env.BUILD_ID}"
            }
          }
        }
        stage('Run Tests') {
          agent { docker { image "${APP_TESTER_IMAGE}:${env.BUILD_ID}" } }
          steps {
              sh "echo 'Testing'"
              sh "python3 manage.py test -v 3 */"
          }
          post {
            always {
              script {
                docker.rmi "${APP_TESTER_IMAGE}:${env.BUILD_ID}"
              }
            }
            failure {
              sh "echo 'Test Failed'"
            }
          }
        }
      }
    }

    stage('Build App Image') {
      steps {
        script {
          docker.build "${APP_IMAGE}:${env.BUILD_ID}"
        }
      }
    }
  }
}

// stage('Deliver') { 
//   // agent { docker { image 'python:3.7' } }
//   steps {
//     sh 'echo > "teste.txt" hello' 
//   }
//   post {
//     success {
//       archiveArtifacts 'teste.txt' 
//     }
//   }
// }
// Send email
// Disabled because of insecurity
// post {
//     always {
//         mail to: 'user@gmail.com',
//         subject: "Jenkins Build: ${currentBuild.fullDisplayName}",
//         body: """
//             Project: ${currentBuild.projectName} ${env.BUILD_ID}
//             Build result: ${currentBuild.result}
//         """
//     }
// }