alias aws-av-rnd='aws sso login --profile av-rnd --use-device-code --no-browser'

# merge k8s configs
export KUBECONFIG=~/.kube/config:~/.kube/config-kansas-gimel:~/.kube/config-kansas-dalet:~/.kube/config-av-rnd
