pipeline {

    agent any

    environment {
        HOST_IP = "{host-ip}"
        PROJECT_TOKEN = "{sonar-projet-token}"
        PROJECT_KEY = "{sonar-project-key}"
        WORKSPACE = pwd()
    }

    stages {

        stage ('Test') {
            agent {
                docker {
                    image 'python:3.11.1-alpine3.16'
                    reuseNode true
                }
            }
            steps {
                sh "pip3 install pytest coverage"
                sh "pytest --junitxml=result.xml"
            }
        }

        stage('Scan') {

            steps {

                script {
                    def scannerHome = tool 'sonarqube';
                    withSonarQubeEnv() {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.projectKey=${PROJECT_KEY} -Dsonar.sources=. -Dsonar.host.url=http://${HOST_IP}:9000 -Dsonar.login=${PROJECT_TOKEN} -X"
                    }
                }

                script {
                    final String url = "http://${HOST_IP}:9000/api/qualitygates/project_status?projectKey=${PROJECT_KEY}"
                    final String response = sh(script: "curl -s $url", returnStdout: true).trim()
                    def data = readJSON text: response;
                 
                    if ("${data.projectStatus.status}" == "ERROR") {
                        currentBuild.result = 'FAILURE'
                        error('Failed quality gates.')
                    }
                }
            }
        }

        stage('Build') {
            steps {
                sh "docker build -t pyapp-img ."
            }
        }

        stage('Deploy') {
            steps {
                sh "docker run -d --name pyapp -p 8000:8000 pyapp-img"
            }
        }
    }
}