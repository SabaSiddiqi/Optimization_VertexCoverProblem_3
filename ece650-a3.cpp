#include<stdio.h>
#include<stdlib.h>
#include<unistd.h>
#include<sys/types.h>
#include<sys/wait.h>
#include<errno.h>
#include<string.h>
#include <signal.h>


int main(int argc, char *argv[]){

	int pipe1[2];
	int pipe2[2];
	char *a[4];
	char buffer[1000];
	
	if(pipe(pipe1)== -1){
		perror("Error:Pipe1 Error");
		exit(1);
	}
	if(pipe(pipe2)== -1){
		perror("Error:Pipe2 Error");
		exit(1);
	}

	pid_t kid_rgen;
	
	if((kid_rgen=fork()) == 0){
		close(pipe1[0]);
		dup2(pipe1[1],STDOUT_FILENO);
		execv("./rgen", argv);
    }
	
	a[0] = (char*)"/bin/bash";
	a[1] = (char*)"-c";
	a[2] = (char*)"python ./ece650-a1.py";
	a[3] = nullptr;
	
	
	pid_t kid_a1= fork();
	
	if(kid_a1==0){
			close(pipe1[1]);
			dup2(pipe1[0],STDIN_FILENO);
			close(pipe2[0]);
			dup2(pipe2[1],STDOUT_FILENO);
			execv ("/bin/bash", a);
			}
	
	pid_t kid_a2= fork();

	if(kid_a2 == 0){
				close(pipe2[1]);
				dup2(pipe2[0],STDIN_FILENO);
				close(pipe2[0]);
				execv("./ece650-a2",nullptr);	
	}
		
	while(fgets(buffer,100,stdin)!=NULL)
		{
		write(pipe2[1],buffer,strlen(buffer));
		}

	kill(kid_rgen, SIGTERM);
	kill(kid_a1, SIGTERM);
	kill(kid_a2, SIGTERM);
	
	return 0;
}


