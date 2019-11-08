pipeline {
    agent any
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
            agent { docker { image 'python:3.7' } }
            steps {
                // NO-OP
                sh 'python3 --version'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build "${IMAGE_NAME}:${env.BUILD_ID}"
                }
            }
        }
        stage('Test') {
            // agent { docker { image 'python:3.7' } }
            steps {
                sh "echo 'TODO run tests'"
            }
            post {
                always {
                    sh "echo 'TODO'"
                }
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
}