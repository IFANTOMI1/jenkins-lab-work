pipeline {
    agent any

    parameters {
        choice(name: 'ENV', choices: ['dev', 'prod'], description: 'Среда для деплоя')
    }

    stages {
        stage('Deploy') {
            steps {
                echo "Deploying to ${params.ENV}"

                sshPublisher(publishers: [
                    sshPublisherDesc(
                        configName: 'osman-nuri', 
                        transfers: [
                            sshTransfer(
                                sourceFiles: 'app.py, Dockerfile',
                                removePrefix: '', 
                                remoteDirectory: '/home/osman-nuri/app'
                            )
                        ], 
                        usePromotionTimestamp: false, 
                        useWorkspaceInPromotion: false, 
                        verbose: true
                    )
                ])
            }
        }
    }

    post {
        always {
            echo "Cleaning up workspace..."
            cleanWs()
        }
    }
}
