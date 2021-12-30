.PHONY: deploy

deploy:
	$(MAKE) deploy-namespace

deploy-namespace:
	kubectl apply -f deploy/namespace.yaml > /dev/null
	kubectl apply -f deploy/configmap_microservice.yaml > /dev/null
