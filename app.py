from aws_cdk import App, Environment, aws_s3, aws_s3_notifications, aws_lambda, aws_ec2, aws_iam, aws_ssm, aws_kms
# from src.constructs.bucket import S3Constructs
# from src.constructs.cloudwatch import SloAlarmsWithCdkStack
from github_cdk.src.constructs.ec2 import *
from github_cdk.src.constructs.iam import LoginRolesStack
from github_cdk.src.constructs.kms import KMSConstructs
from github_cdk.src.constructs.ssm import *
from typing import Any
from typing import Optional
from constructs import Construct


def _get_env_config(scope: Construct, key: str) -> Any:
    env_name = scope.node.try_get_context("env") or "dev"
    env_config = scope.node.try_get_context(env_name) or {}
    return env_config.get(key)
    
# env_details = aws_cdk.Environment(account="389275668707", region="us-east-1")
# env_details = {
#     "account" : "389275668707",
#     "region" : "us-east-1"
# }




def create_app():
    app = App()
    account = _get_env_config(app, "account")
    region = _get_env_config(app, "region")
    env_name = app.node.try_get_context("env") or "dev"

    repository_name = "aws-cdk-resources"
    stack_name = f"{repository_name}-stack"
    
    # ec2_stack = CdkSimpleUbuntuInstanceAsg(
    #     scope = app,
    #     env_name=env_name,
    #     id = stack_name,
    #     account = account,
    #     region = region
    #  )


    login_roles = LoginRolesStack(
        scope = app,
        stack_id= stack_name,
        env = env_name
        )


    app.synth()

if __name__ == "__main__":
    create_app()
