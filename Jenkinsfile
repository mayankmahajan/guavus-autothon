pipeline {
  agent any
  
  stages {
    
    stage("Build Test"){
        
        stages {
            stage ("Install required Python dependencies inside test docker"){
                steps {
                        script{
                                AUTOMATION_PATH = "automation/"
                        }
                        sh "pip freeze | grep -i nimble"
                        echo "Installing solution docker python dependencies inside docker."
                        sh "cd ${AUTOMATION_PATH} && pip install --user -r requirements.txt"
                        echo "Dependencies installed."
                    }
            }

            stage ("Health Check BPL") {
                steps {
                        
                        echo "Running pytest command for Healthcheck inside docker."
                        sh "python -m pytest tests/test.py"
                    }
            }
            

        }
    }
  }
    post {
                always {
                      allure includeProperties: false, jdk: '', results: [[path: 'automation/target/artifacts/allure/']]
                      publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: 'automation/target/artifacts/', reportFiles: 'report.html', reportName: 'HTML Report', reportTitles: ''])
        }
    }

}