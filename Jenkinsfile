pipeline {
  agent any
  
  stages {
    
    stage("Build Test"){
        
        stages {
            stage ("Install required Python dependencies inside test docker"){
                steps {
                        
                        sh "virtualenv venv --python=python2.7 && source venv/bin/activate && pip install -r requirements.txt && deactivate"
                        
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

}