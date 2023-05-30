
Creer le workspace et mettre sur Github 
Sur le terminal:
	- creer un dossier catkin_ws : 
 		-> mkdir catkin_ws
	- puis creer un dossier src : 
 		-> mkdir src
	- Entrer dans src et faire un git clone: 
 		-> git clone https://github.com-			AndriamananjaraLturtle_regulation_lafatra_feelminho
	- Créer un package avec pour nom turtle_regulation_lafatra_feelminho et pour dépendance rospy, roscpp, std_msgs, geometry_msgs et turtlesim : 
		-> catkin_create_pkg turtle_regulation_lafatra_feelminho rospy roscpp std_msgs geometry_msgs turtlesim
	- Dans src, faire un catkin build : 
 		-> ~/catkin_ws$ catkin build 


Pour ajouter dans github: 
	- Entrer dans turtle_regulation_lafatra_feelminho
	- commandes sur terminal: 
		-> git add
		-> git commit -m "votre message de commit"
		->git push

	- Puis entrer : Username for 'https://github.com' et mot de passe
	- Verifier sur github.


Pour executer le package :

	-> Ouvrir dans un premier terminal et tapper : roscore

	-> Dans un second terminal : Lancer : ~$ rosrun turtlesim turtlesim_node 

	-> Dans le troisieme terminal :
		- Rendre le code executabe : chmod +x set_way_point.py
		- Sourcer le package [dans le source de catkin build] avec : source devel/setup.bash
		- build le package : catkin build
		- Remapping avec : rosrun turtle_regulation_lafatra_feelminho set_way_point.py /cmd_vel:=/turtle1/cmd_vel /pose:=/turtle1/pose _kp:=7
