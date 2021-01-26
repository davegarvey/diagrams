from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.onprem.inmemory import Redis
from diagrams.onprem.database import Mongodb
from diagrams.tyk.component import Gateway


# use outformat param to set output format
with Diagram("Tyk Minimal Deployment", show=False, direction="TB"):
    ELB("lb") >> EC2("web") >> RDS("userdb") >> Gateway("Gateway 2")