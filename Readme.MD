# Deploy Llama 2 using SageMaker Jumpstart
This repository contains code and resources for deploying the Llama2 model on AWS using SageMaker Jumpstart.

## About Llama2
Llama 2 pretrained models are trained on 2 trillion tokens, and have double the context length than Llama 1. Its fine-tuned models have been trained on over 1 million human annotations.
link:https://ai.meta.com/llama/

## Prerequisites
Before you begin, ensure you have met the following requirements:
* You have an AWS account
* You have installed and configured the AWS CLI
* You have installed Python 3.x and Jupyter Notebook

## Using Llama2 on AWS
To use Llama2 on AWS, follow these steps:
1. Open Amazon SageMaker: Log into your AWS console and navigate to the Amazon SageMaker service.
2. Create a Notebook Instance: Click on "Notebook instances" in the left-hand panel, and then click on the "Create notebook instance" button.

3. Configure the Notebook Instance:
* Give your notebook instance a name.
* Choose an instance type. This will depend on the requirements of your model.
* Choose an IAM role that has the necessary permissions. If you don't have one, you can create a new role.
* Then click on "Create notebook instance" at the bottom of the page.
4. Open Jupyter: Once your notebook instance status is "InService", click on "Open Jupyter" to open the Jupyter dashboard.
5. Clone this repository to notebook.
6. Run Your Notebook: Once your notebook is ready, you can run it. In Jupyter, click on "Cell" in the menu, and then click on "Run All" to run all the cells in your notebook.

## Contributing to Llama2 on AWS
To contribute to Llama2 on AWS, follow these steps:
1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.


## License
MIT
