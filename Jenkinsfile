pipeline {
  agent any
  
  stages {
    
    stage("Build Test"){
        
        stages {
            stage ("Install required Python dependencies"){
                steps {
                        
                        sh "virtualenv venv --python=python2.7 && source venv/bin/activate && pip install -r requirements.txt && deactivate"
                        
                    }
            }

            stage ("Sample Tests") {
                steps {
                        
                        sh " source venv/bin/activate && python -m pytest tests/test.py && deactivate"
                    }
            }
            
            stage('Export test results to csv') {
                steps {
                    sh 'source venv/bin/activate &&  python dump_csv.py ${currentBuild.currentResult} && deactivate'
                } 
            }

        }
    }
  }

}
