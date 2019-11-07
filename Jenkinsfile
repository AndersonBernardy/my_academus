pipeline {
    agent { docker { image 'python:3.7' } }
    options {
        // Stop build if a step fail
        skipStagesAfterUnstable()
        // Only keep the 10 most recent builds
        buildDiscarder(logRotator(numToKeepStr:'10'))
    }
    environment {
        IMAGE_NAME = 'my_academus'
    }
    stages {
        stage('Compile') {
            // agent { docker { image 'python:3.7' } }
            steps {
                // NO-OP
                sh 'python3 --version'
            }
        }
        stage('Test') {
            // agent { docker { image 'python:3.7' } }
            steps {
                sh "echo 'TODO run tests'"
                // Example: sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    sh "echo 'TODO'"
                }
            }
        }
        stage('Build') {
            // agent { docker { image 'python:3.7' } }
            steps {
                docker.build("${IMAGE_NAME}:${env.BUILD_ID}")
            }
        }
        stage('Deliver') { 
            // agent { docker { image 'python:3.7' } }
            steps {
                sh 'echo > "teste.txt" hello' 
            }
            post {
                success {
                    archiveArtifacts 'teste.txt' 
                }
            }
        }
    }
    // Send email
    post {
        always {
            mail to: 'andersonbmartinelli@gmail.com',
            subject: "Jenkins Build: ${currentBuild.fullDisplayName}",
            body: """
                Project: ${currentBuild.projectName} ${env.BUILD_ID}
                Build result: ${currentBuild.result}
            """
        }
    }
}