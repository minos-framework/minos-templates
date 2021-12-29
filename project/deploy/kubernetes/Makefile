build:
	$(MAKE) build-namespace

build-namespace:
	kubectl apply -f namespace.yaml > /dev/null
	kubectl apply -f configmap_microservices.yaml > /dev/null