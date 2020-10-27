.DEFAULT_GOAL := run

gen-rpc:
	pipenv run python -m grpc_tools.protoc -I./proto --python_out=. --grpc_python_out=. ./proto/helloworld.proto

serve:
	pipenv run python server.py

run:
	pipenv run python client.py
