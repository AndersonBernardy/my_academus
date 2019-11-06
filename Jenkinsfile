pipeline {
    agent none
    options {
        skipStagesAfterUnstable()
    }
    stages {
        // stage('Build') {
        //     agent {
        //         docker {
        //             image 'python:3.7'
        //         }
        //     }
        //     steps {
        //         sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        //     }
        // }
        // stage('Test') {
        //     agent {
        //         docker {
        //             image 'qnib/pytest'
        //         }
        //     }
        //     steps {
        //         sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
        //     }
        //     post {
        //         always {
        //             junit 'test-reports/results.xml'
        //         }
        //     }
        // }
        stage('Deliver') { 
            agent {
                docker {
                    image 'my_academus' 
                }
            }
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
}