build:
	$(MAKE) build-namespace

build-namespace:
	kubectl apply -f deploy/namespace.yaml > /dev/null
	kubectl apply -f deploy/configmap_microservices.yaml > /dev/null