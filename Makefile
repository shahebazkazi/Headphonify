AWS_REGION = ap-south-1
AWS_ACCOUNT_ID = 895471402311
MS1 = wandrstar_template

GIT_HASH = $(TAG)

.PHONY: build
build:
	docker-compose build

.PHONY: run
run:
	docker-compose up

.PHONY: tag
tag:
	docker tag $(MS1):latest $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com/$(MS1):$(GIT_HASH)
	
.PHONY: login
login:
	aws ecr get-login-password --region $(AWS_REGION) | docker login --username AWS --password-stdin $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com

.PHONY: push
push: login
	docker push $(AWS_ACCOUNT_ID).dkr.ecr.$(AWS_REGION).amazonaws.com/$(MS1):$(GIT_HASH)
