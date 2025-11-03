pipeline {
    agent any // Run on any available Jenkins agent

    environment {
        // Store Docker Hub credentials securely in Jenkins
        // Go to Manage Jenkins > Credentials > System > Global credentials
        // Add a "Username with password" credential with ID 'docker-hub-creds'
        DOCKER_CREDS = credentials('docker-hub-creds')
        DOCKER_IMAGE = "your-docker-username/ml-app:${env.BUILD_NUMBER}"
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                // This checks out the code from the repo Jenkins is monitoring
                git branch: 'master', url: 'https://github.com/your-username/my-mlops-repo.git'
            }
        }

        stage('2. Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image: ${DOCKER_IMAGE}"
                    // 'sh' is the step for running shell commands
                    sh "docker build -t ${DOCKER_IMAGE} ."
                }
            }
        }

        stage('3. Push to Docker Hub') {
            steps {
                script {
                    echo "Logging in and pushing image..."
                    // Use the secure credentials from the environment block
                    sh "echo $DOCKER_CREDS_PSW | docker login -u $DOCKER_CREDS_USR --password-stdin"
                    sh "docker push ${DOCKER_IMAGE}"
                }
            }
        }

        stage('4. Deploy (Simulation)') {
            steps {
                // In a real MLOps pipeline, this stage would deploy to
                // Kubernetes, AWS, etc. Here, we just run it.
                echo "Deploying container..."
                // We run it, sleep, then stop it to show it works
                sh "docker run -d -p 5000:5000 --name ml_app_${env.BUILD_NUMBER} ${DOCKER_IMAGE}"
                sh "sleep 10"
                sh "docker stop ml_app_${env.BUILD_NUMBER}"
                sh "docker rm ml_app_${env.BUILD_NUMBER}"
            }
        }
    }

    post {
        always {
            // Clean up the built image from the Jenkins server
            echo "Cleaning up..."
            sh "docker rmi ${DOCKER_IMAGE}"
        }
    }
}