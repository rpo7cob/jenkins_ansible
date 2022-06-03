pipeline {
    agent any

    stages {
        stage('hello-world') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Dev Branch') {
            steps {
                echo 'Building from Dev Branch'
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
