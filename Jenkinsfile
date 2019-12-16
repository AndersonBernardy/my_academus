pipeline {
  agent any
  options {
    // Stop build if a step fail
    skipStagesAfterUnstable()
    // Only keep the 10 most recent builds
    buildDiscarder(logRotator(numToKeepStr:'10'))
  }
  environment {
    BASE_IMAGE_DOCKERFILE_DIR = 'setup/base'
    BASE_IMAGE = 'django-mariadb-base'
    TESTER_IMAGE = 'django-selenium-tester'
    TESTER_IMAGE_DOCKERFILE_DIR = 'setup/tester'
    APP_IMAGE = 'my-academus-app'
    APP_IMAGE_DOCKERFILE_DIR = 'setup/app'
    APP_TESTER_IMAGE = 'my-academus-tester'
    APP_TESTER_IMAGE_DOCKERFILE_DIR = 'setup/app-tester'
  }

  stages {
    stage('Setup') {
      stages {
        stage('Setup Base Image') {
          steps {
            script {
              def image = sh "docker images -q ${BASE_IMAGE}"
              if (image != "${BASE_IMAGE}"){
                sh "echo 'Building Image: ${BASE_IMAGE}'"
                sh "docker build -f ${BASE_IMAGE_DOCKERFILE_DIR}/Dockerfile -t ${BASE_IMAGE} ."
                // docker.build("${BASE_IMAGE}", "${BASE_IMAGE_DOCKERFILE_DIR}")
              } else {
                sh "echo 'Image already built: ${BASE_IMAGE}'"
              }
            }
          }
        }
        stage('Setup Base Tester Image') {
          steps {
            script {
              def image = sh "docker images -q ${TESTER_IMAGE}"
              if (image != "${TESTER_IMAGE}"){
                sh "echo 'Building Image: ${TESTER_IMAGE}'"
                sh "docker build -f ${TESTER_IMAGE_DOCKERFILE_DIR}/Dockerfile -t ${TESTER_IMAGE} ."
                // docker.build("${TESTER_IMAGE}", "${TESTER_IMAGE_DOCKERFILE_DIR}")
              } else {
                sh "echo 'Image already built: ${TESTER_IMAGE}'"
              }
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
              sh "docker build -f ${APP_TESTER_IMAGE_DOCKERFILE_DIR}/Dockerfile -t ${APP_TESTER_IMAGE}:${env.BUILD_ID} ."
              // docker.build("${APP_TESTER_IMAGE}:${env.BUILD_ID}", "${APP_TESTER_IMAGE_DOCKERFILE_DIR}")
            }
          }
        }
        stage('Run Tests') {
          agent { docker { image "${APP_TESTER_IMAGE}:${env.BUILD_ID}" } }
          steps {
              sh "echo 'Testing'"
              sh "python3 manage.py runserver localhost:8000"
              sh "python3 manage.py test -v 3 */"
          }
          post {
            always {
              script {
                docker.rmi("${APP_TESTER_IMAGE}:${env.BUILD_ID}")
              }
            }
            failure {
              sh "echo 'Test Failed'"
            }
          }
        }
      }
    }

    stage('Build') {
      steps {
        script {
          sh "docker build -f ${APP_IMAGE_DOCKERFILE_DIR}/Dockerfile -t ${APP_IMAGE}:${env.BUILD_ID} ."
          // docker.build("${APP_IMAGE}:${env.BUILD_ID}", "${APP_IMAGE_DOCKERFILE_DIR}")
        }
      }
    }
  }
}