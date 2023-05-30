import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from math import atan2

 

# Variable globale pour stocker la pose de la tortue
current_pose = Pose()

 

# Callback appelée lorsqu'un message est reçu sur le topic "pose"
def pose_callback(msg):
    global current_pose
    current_pose = msg

 

# Initialisation du nœud ROS
rospy.init_node('turtle_regulation_nom1_nom2')

 

# Souscription au topic "pose" avec la fonction de rappel pose_callback
rospy.Subscriber('pose', Pose, pose_callback)

 

# Définition du waypoint avec les coordonnées (7, 7)
waypoint = (7, 7)

 

# Calcul de l'angle désiré
desired_angle = atan2(waypoint[1] - current_pose.y, waypoint[0] - current_pose.x)

 

# Calcul de l'erreur
error = atan2(atan2(waypoint[1] - current_pose.y, waypoint[0] - current_pose.x) - current_pose.theta)

 

# Constante de proportionnalité Kp (à ajuster selon les besoins)
Kp = 1.0

 

# Calcul de la commande en cap du robot
command = Kp * error

 

# Création d'un éditeur pour publier sur le topic "cmd_vel"
pub = rospy.Publisher('cmd_vel', Twist, queue_size=10)

 

# Fonction d'aide pour créer un objet Twist avec la vitesse angulaire en z
def create_twist(angular):
    twist = Twist()
    twist.angular.z = angular
    return twist

 

# Boucle principale
rate = rospy.Rate(10)  # Fréquence de publication (10 Hz)
while not rospy.is_shutdown():
    # Publication de la commande en cap
    pub.publish(create_twist(command))

 

    rate.sleep()
