pipeline {
    agent any

    stages {
        stage('hello-world') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Stage Branch') {
            steps {
                echo 'Building from Stage Branch'
            }
        }        
        stage('Uptime') {
            steps {
                sh 'uptime'
            }
        }
        stage('Exit Test') {
            steps {
                sh 'exit'
            }
        }        
        stage('sleep mode') {
            steps {
                sleep 10
            }
        }        
    }
}
