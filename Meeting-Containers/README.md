# Docker

## Εναλλακτικά container registry
Για την χρήση εναλλακτικών container registry, βάλτε το url του registry πριν από το όνομα της εικόνας. Έτσι, θα πρέπει να κάνετε:

```sh
$ docker build -t registry.gitlab.com/mygroup/myproject/myimage
```

Το DockerHub προσφέρει την δυνατότητα για ιδιωτικά containers, αλλά μόνο αν πληρώσετε. Όμως άλλα registries το δίνουν δωρεάν. Μερικά αξιόλογα registries:
- [registry.gitlab.com](https://docs.gitlab.com/ee/user/packages/container_registry/): Gitlab.com container registry
- [ghcr.io](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry): Github container registry
- [quay.io](https://docs.quay.io/solution/getting-started.html): Εναλλακτική του DockerHub από την RedHat
- [gcr.io](https://cloud.google.com/container-registry): Google Container Registry

Για να κάνετε push μια εικόνα, πρέπει να κάνετε [docker login](https://docs.docker.com/engine/reference/commandline/login/) για κάθε registry. Θα χρειαστεί για για να κάνετε pull ιδιωτικές εικόνες.

Αν έχετε και όρεξη, να μια άσκηση: [Deploy a docker registry](docs.docker.com/registry/deploying)

## Δομή docker

Η ιεραρχία είναι η εξής:  
- **docker**: Η εντολή με την οποία αλληλεπιδράτε ως χρήστες
- **dockerd**: Ενας δαίμονας που τρέχει ως root στο παρασκήνιο και ανταποκρίνεται στα αιτήματα του docker cli.
- **containerd**: Ένα επίπεδο πιο κάτω από το dockerd. Είναι ο δαίμονας που τελικά «κάνει πράγματα» (πιο χαμηλού επιπέδου).
- Και τελικά τα containers. Υπάρχουν κι εδώ πολλές λεπτομέρειες, αλλά θα της αφήσω χάριν χρόνου. Χρησιμα keywords: containerd-shim, runc, Open Container Interface (OCI), Linux Namespaces

Τέλος, λίγοι ακόμα όροι για τους περιπετειώδεις: Open Container Initiative (OCI), Common Runtime Interdace (CRI), nerdctl, crictl, CRI-O, docker-in-docker, Common Network Interface (CNI)

# Kubernetes

Τα containers αυτοματοποιούν την εγκατάσταση προγραμμάτων. Όμως μπορούμε να κάνουμε περισσότερα: Αυτοματοποιώντας τα containers. Αυτό κάνει το Kubernetes.

Το k8s σημαίνει kubernetes.

Τρία βασικά πράγματα να έχετε υπ'όψην:
1. RTFM. Τα tutorials είναι συχνά πολύ παλιά ή δίνουν κακές συμβουλές.
2. Το Manual κάποιες φορές λέει βλακείες. Μία άλλη χρήσιμη πηγή πληροφοριών είναι τα issues στο GitHub, όπου εξηγούνται πολλά από τα πράγματα για τα οποία η τεκμηρίωση είναι ελλιπής.
3. Όλοι θέλουν να σας πουλήσουν κάτι. Και αυτό φαίνεται στα manual. Τα forum είναι συχνά πολύ πιο αξιόπιστα όταν προκύπτει αυτό.

## Εγκατάσταση

Υπάρχουν πολλοί τρόποι να εγκαταστήσετε το «Kubernetes». Αλλά να έχετε υπ'όψην πως Kubernetes δεν είναι ένα συγκεκριμένο πράγμα, αλλά ένα σύνολο distribution (ακριβώς όπως τα Linux distributions). Έτσι υπάρχουν και πολλά distribution kubernetes. Αναφορικά:

- **minikube**: Τοπικό kubernetes για δοκιμές
- **kubeadm**: Το εργαλείο που χρησιμοποιείται για την δημιουργία kubernetes cluster (Αρκετά χαμηλού επιπέδου)
- **kind**: Kubernetes in Docker
- **k3s**: Kubernetes για χαμηλής απόδοσης συστήματα (Edge-computing)
- **Rancher**: Ολοκληρωμένο distribution από την Suse
- **OpenShift**: Ολοκληρωμένο distribution από την RedHat
- **kubespray**: Ολοκληρωμένο distribution όμως εξαιρετικά προσαρμόσιμο και ταυτόχρονα περίπλοκο. Αποτελείται από ansible playbooks (δλδ. scripts) που τρέχετε εσείς χειροκίνητα. Σας είπα πως χρησιμοποιώ Arch btw?

Υπάρχουν επίσης υπηρεσίες που παρέχουν Kubernetes-ως-υπηρεσία. Αν είστε φτοιαγμένοι από χρήματα, πάτε εδώ:
- **AKS**: Azure Kubernetes Service
- **EKS**: Amazon Elastic Kubernetes Service
- **GCE**: Google Cloud Engine
- **RedHat OpenShift**
- **VMware Tanzu**
- **Docker EE**: Μην ξεχνάτε, το docker είναι εταιρία. Απλά διαχειρίζεται open source κώδικα.

Υπάρχουν και πολλά άλλα, αλλά αυτά είναι τα βασικά που θα δείτε στις αναζητήσεις σας.

### Minikube

Εγκαταστήστε το minikube. Αν δεν είστε σίγουροι πώς, δείτε το [quickstart](https://minikube.sigs.k8s.io/docs/start/).

Εγκαταστήστε το kubectl, ή εναλλακτικά χρησιμοποιήστε το kubectl του minikube:

```sh
$ alias kubectl="minikube kubectl --"
```

Θα τρέξω το minikube στο docker του συστήματος, όμως μπορείτε να χρησιμοποιήσετε και virtual machines (με virtualbox ή kvm):

Εγκαθιστώ το docker
```sh
# pacman -S docker
# systemctl enable docker
```

Για να μπορώ να εκτελώ εντολές docker χωρίς sudo, προσθέτω τον εαυτό μου στην ομάδα docker
```sh
# groupadd docker
# usermod -aG docker $USER
```

Ρυθμίζω το minikube ώστε να χρησιμοποιεί το docker
```sh
$ minikube config set driver docker
```

Τέλος, κάνω επανεκκίνηση, επιστρέφω στο τερματικό, οπλίζομαι με αρκετή υπομονή και τρέχω:
```sh
$ minikube start
```

Στο τέλος, πρέπει να μπορείτε να μπορείτε πάρετε την παρακάτω έξοδο
```sh
$ kubectl get node
NAME       STATUS   ROLES                  AGE   VERSION
minikube   Ready    control-plane,master   98s   v1.23.3
```

## Βασικές Έννοιες

Το kubernetes στην γενική περίπτωση τρέχει σε πολλούς κόμβους (nodes - δηλαδή, υπολογιστές). Κάποια από αυτούς είναι κόμβοι ελέγχου (control nodes), συχνά περισσότεροι από 1 και μονός αριθμός. Οι κόμβοι ελέγχου είναι υπεύθυνοι για την διαχείρηση του cluster. Εμείς μιλάμε σε έναν από αυτούς τους κόμβους με το εργαλείο kubectl για την επικοινωνία μας με το cluster.

Για απλότητα, το minikube δημιούργησε έναν μόνο κόμβο ελέγχου στον οποίο μπορούμε να πειραματιστούμε.

### Resources

Μπορούμε να «προγραμματίσουμε» το kubernetes δημιουργώντας διάφορα resources, τα οποία συνήθως αναπαριστούμε σε yaml (ή, ισοδύναμα, σε json).

#### Pod

Δημιουργήσουμε ένα αρχείο pod.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx:1.21.6
```

Τα `apiVersion` και `kind` είναι αυστηρά ορισμένα για τα Pods. Για άλλα resources, θα διαφέρουν. Το `metadata` ορίζει μεταδεδομένα, όπως είναι το όνομα του resource (εδώ nginx) και τα labels (που θα δούμε αργότερα).

Το Pod ορίζεται κατά βάση στο `spec`, όπου ορίζουμε πως το `Pod` αυτό περιέχει ένα μόνο container, το nginx. Σε υψηλό επίπεδο, ένα `Pod` αναπαριστά έναν εικονικό server. Κάθε `Pod` έχει δηλαδή την δική του IP και συμπεριφέρεται, μέσα στο δίκτυο του cluster, σαν ένας υπολογιστής. Σαν επιπλέον ανάγνωση, παραθέτω ένα [blog post](https://ronaknathani.com/blog/2020/08/how-a-kubernetes-pod-gets-an-ip-address/) που εξηγεί την μαγεία πίσω από όλο αυτό αρκετά καλά.

Τώρα μπορούμε να στείλουμε το αρχείο αυτό στο cluster:
```sh
$ kubectl apply -f pod.yaml
pod/nginx created
```

Οπότε, τώρα αν κοιτάξουμε τα pods:
```sh
$ kubectl get pod
NAME    READY   STATUS              RESTARTS   AGE
nginx   0/1     ContainerCreating   0          17s
```

Βλέπουμε πως το pod δεν είναι έτοιμο. Αν περιμένουμε κάποια ώρα όμως, αυτό αλλάζει:
```sh
$ kubectl get pod
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          2m
```

Τώρα τι έγινε από πίσω; Το kubernetes κατέβασε την εικόνα του nginx, την έβαλε σε ένα «Pod», την εκτέλεσε και... ε, αυτό είναι όλο. Για να επικοινωνήσουμε με το nginx που τρέχει στο Pod πρέπει να ανοίξουμε ένα port, όπως και στο απλό docker.

Οπότε, πάμε πάλι στο pod.yaml και προσθέτουμε το port στο container:

```yaml
  # ...
  containers:
  - name: nginx
    image: nginx:1.21.6
    ports:
    - containerPort: 80
```

Τώρα, διαγράφουμε το αρχικό pod και κάνουμε πάλι apply:
```sh
$ kubectl delete pod nginx
pod "nginx" deleted
$ kubectl apply -f pod-2.yaml
pod/nginx created
$ kubectl get po
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          12s
```

Την δεύτερη φορά το Pod ξεκίνησε πολύ πιο γρήγορα, αφού έχουμε ήδη κατεβάσει την εικόνα του container. Όμως και πάλι, δεν έχουμε πρόσβαση στον server μας.

```sh
$ curl http://localhost
curl: (7) Failed to connect to localhost port 80 after 6 ms: Απόρριψη σύνδεσης
```

Αυτό γίνεται γιατί port εκτέθηκε όντως στο εσωτερικό δίκτυο του kubernetes cluster. Όμως, τουλάχιστον με το minikube, δεν έχουμε πρόσβαση σε αυτό το δίκτυο από προεπιλογή.

Μία γρήγορη λύση είναι να τρέξουμε την εντολή:
```sh
$ kubectl port-forward pod/nginx 8080:80
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
```

Τώρα, αν πάμε στην διεύθυνση [http://localhost:8080](http://localhost:8080), θα δούμε το site μας!

#### Deployment

Ας υποθέσουμε, τώρα, πως για κάποιον λόγο το container μας έχει ένα bug και σβήνει. Στο παραδοσιακό docker, είμαστε εμείς υπεύθυνοι να το επαναφέρουμε. Υπάρχει κάποιος αυτοματισμός μέσω του `--restart=always`, όμως δεν υπάρχει συνεννόηση ανάμεσα σε διαφορετικούς κόμβους του cluster.

Το Deployment αντιμετοπίζει αυτό το πρόβλημα. Το πώς, δηλαδή, αυτοματοπιούμε την δημιουργία pods. Έτσι, στο deploy.yaml γράφουμε:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21.6
        ports:
        - containerPort: 80
```

Τα `apiVersion` και `kind` είναι και πάλι σταθερά για όλα τα Deployment. Το `metadata` είναι ίδιο με το Pod, όμως εδώ βλέπουμε το `labels`, το οποίο είναι ένα map string->string. Τα στοιχεία αυτά μπορούν να χρησιμοποιηθούν για την επιλογή ενός ή περισσοτέρων resources.

Στο `spec` υπάρχουν τρία στοιχεία: To `replicas`, που δηλώνει πόσες φορές θέλουμε να τρέξουμε την εφαρμογή ώστε σε περίπτωση που μία αποτύχει, οι υπόλοιπες να συνεχίσουν να αποκρίνονται. Το `selector` είναι είδους `matchLabels` και ψάχνει για Pods με το label `app` ίσο με την τιμή `nginx`. Το Deployment είναι, δηλαδή, ένα πρόγραμμα που διαχειρίζεται ένα ή περισσότερα Pod. Τέλος, ορίζουμε το `template`, το οποίο ορίζει την κατάσταση στην οποία θέλουμε να είναι τα Pod μας.

Τώρα, διαγράφουμε το προηγούμενο pod, και εφαρμόζουμε το deployment:
```sh
$ kubectl delete pod/nginx
pod "nginx" deleted
$ kubectl apply -f deploy-1.yaml
deployment.apps/nginx created
$ kubectl get pod,deployment
NAME                        READY   STATUS    RESTARTS   AGE
pod/nginx-cb69f686c-klqbg   1/1     Running   0          24s
pod/nginx-cb69f686c-lvvt9   1/1     Running   0          24s
pod/nginx-cb69f686c-mhtp9   1/1     Running   0          24s

NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/nginx   3/3     3            3           25s
```

Βλέπουμε πως δημιουργήθικαν επιτυχώς τα 3 Pod που ορίσαμε στο `replicas`.

#### Service

Για την πρόσβαση στο deployment χωρίς να ορίζουμε κάθε φορά ένα συγκεκριμένο
node μπορούε να δημιουργήσουμε ένα service. Για λόγους απλότητας, θα ασχοληθούμε
μόνο με τα Service τύπου ClusterIP, τα οποία είναι προσβάσιμα μόνο μέσα στο
kubernetes cluster. Έτσι, δημιουργούμε το παρακάτω resource:

```sh
apiVersion: v1
kind: Service
metadata:
  name: frontend
  labels:
    app: frontend
spec:
  selector:
    app: frontend
  ports:
    - port: 80
      protocol: TCP
```

Εδώ ορίζουμε ένα service που λειτουργεί σε υψηλό επίπεδο, σαν ένα pod
(παίρνει δηλαδή το δικό του ip) το οποίο δεν απαντά το ίδιο σε requests,
αλλά τα στέλνει στα pods με label `app: frontend` (με round-robin).

```sh
$ kubectl apply -f svc-2.yaml
$ kubectl port-forward service/frontend 8080:80
```

Επιπλέον keywords για τους περιπετειώδεις: Service, ClusterIP, NodePort, LoadBalancer, StatefulSet, DaemonSet, helm, ingress, haproxy-ingress, kubelet, kube-proxy, Operator pattern

