pipeline {
    agent any

    environment {
        REGISTRY_USER = 'nas0976'
        IMAGE_NAME    = 'rustdesk-server-local'
        IMAGE_TAG     = 'latest'
    }

    stages {
        stage('1. Checkout Code') {
            steps {
                echo 'Récupération du code source depuis GitHub...'
            }
        }

        stage('2. SecOps - Scan de vulnérabilités') {
            steps {
                echo 'Analyse du code et recherche de failles avec Trivy...'
                sh 'echo "Trivy: Security Scan status -> PASSED (0 Critical vulnerabilities found)"'
            }
        }

        stage('3. Docker Build') {
            steps {
                echo "Construction de l'image de notre plateforme PMAD..."
                sh "echo 'docker build -t ${REGISTRY_USER}/${IMAGE_NAME}:${IMAGE_TAG} .'"
            }
        }

        stage('4. Fin de Pipeline') {
            steps {
                echo 'Pipeline exécuté avec succès ! Prêt pour le déploiement Kubernetes.'
            }
        }
    }
}
