#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <string.h>

#define Constant 5000
#define white 0
#define gray 1

using namespace std;


typedef struct Linked_List_Node{

    int data;
    struct Linked_List_Node *next;

}Node;

typedef struct Node_Data{

    int vertex_value;
    int vertex_direction;
    Node *head;

}ND,Linked_List[Constant];

typedef struct Graph_Data{

    int no_of_vertex;
    Linked_List list;
    int edge_pair;

}Graph;

typedef struct Queue_Data{

    int u,v;
    int data[Constant];
    int qcount;

}Queue;


/*---------------------- Fuctions Start ---------------------------------*/

int color[Constant]={0};

void add_vertex(int no_of_vertex, Graph *Graph){

    Graph->no_of_vertex = no_of_vertex;
    int v;

    for (v=0;v<no_of_vertex;v++){   //update vertex values in node data
        Graph->list[v].head=NULL;
        Graph->list[v].vertex_value=v;
        Graph->list[v].vertex_direction=-1;
    }
}

bool edge_exist_check(int e1, int e2, Graph *Graph, char var){

    bool exist=true;
	if(var=='s'){
		if(e1<0 || e1>=Graph->no_of_vertex || e2<0 || e2>=Graph->no_of_vertex){
        fprintf(stderr,"Error: edge does not exist.\n");
		exist=false;
		}
		else {
        exist=true;}
		}
    //cout << exist << endl;
    return exist;
}

void add_edges(int no_of_edges,int edges[],Graph *Graph){

    int edge_v1,edge_v2;
    int e=0;

    Graph->edge_pair=no_of_edges/2;

    Node *temp;
    Node *head_temp;


    while(e<no_of_edges-1){ // check all edge pairs

        edge_v1=edges[e];
        edge_v2=edges[e+1];

        if (edge_v1!=edge_v2){
            head_temp=Graph->list[edge_v1].head;
            while (head_temp){
                if ( edge_v2==head_temp->data && edge_v1==Graph->list[edge_v1].vertex_value){
                    break;
                }
                head_temp=head_temp->next;
            }
            if (!head_temp){
                temp=(Node*)malloc(sizeof(Node));
                temp->data=edge_v2;
                temp->next=Graph->list[edge_v1].head;
                Graph->list[edge_v1].head=temp;
                temp=(Node*)malloc(sizeof(Node));
                temp->data=edge_v1;
                temp->next=Graph->list[edge_v2].head;
                Graph->list[edge_v2].head=temp;
            }
        }
        e+=2;
    }
}

void initialize_graph(Graph *Graph){
    Node *temp1;
    Node *temp2;
    int count;

    for (count=0;count<Graph->no_of_vertex;count++){
        temp1=Graph->list[count].head;
        while (temp1!=0){
            temp2=temp1;
            temp1=temp1->next;
            free(temp2);
            temp2=NULL;
        }
        Graph->list[count].head=NULL;
    }
    Graph->no_of_vertex=Graph->edge_pair=0;
}

void initialize_color(Graph *Graph){
    int elem;
    for(elem=0;elem<Constant;elem++){
        color[elem]=white;
    }
    for(elem=0;elem<Graph->no_of_vertex;elem++){
        Graph->list[elem].vertex_direction=-1;
    }
}

void initialize_queue(Queue *Queue){
    Queue->u=0;
    Queue->v=0;
    Queue->qcount=0;
}

void enqueue(int point1, Queue *Queue){
    Queue->data[Queue->v]=point1;
    Queue->v=(Queue->v + 1) % Constant;
    Queue->qcount=Queue->qcount+1;
}

int dequeue(Queue *Queue){
    int result;
    result = Queue->data[Queue->u];
    Queue->u=(Queue->u + 1) % Constant;
    Queue->qcount=Queue->qcount-1;
    return result;
}

void shortest_path(int point1,int point2,Graph *Graph){
    int output;
    Queue Queue;
    Node *head_temp;

    initialize_color(Graph);
    initialize_queue(&Queue);
    color[point1]=gray;
    enqueue(point1,&Queue);
    while (Queue.qcount!=0){
        output = dequeue(&Queue);
        head_temp= Graph->list[output].head;
        while (head_temp){
            if(color[head_temp->data]==white){
                color[head_temp->data]=gray;
                enqueue(head_temp->data,&Queue);
                Graph->list[head_temp->data].vertex_direction=output;
            }
            head_temp=head_temp->next;
        }
    }
}

void display_path(int from,int to,Graph *Graph){
    ND n;
    n=Graph->list[to];
    if(n.vertex_direction!=-1){
        display_path(from,n.vertex_direction,Graph);
        fprintf(stdout,"-%d",to);
		fflush(stdout);
    }
    else {
        if(n.vertex_value==from){
            fprintf(stdout,"%d",to);
			fflush(stdout);
        }
        else{
            fprintf(stderr,"Error: path doesn't exist. \n");
            return;
        }
    //fflush(stdout);
	}
	//fprintf(stdout,"\n");
	fflush(stdout);
}

/*-----------------------Main Starts ---------------------------------*/

int main ()
{   // variable initialization
    char input[Constant];
    char command;
    Graph Graph;
    int no_of_vertex;
    char *split=" {}<>,E";
    char *token;
    int e,i,e1,e2;
    int edges[500];
    bool check;
    int point1,point2;

    while (fgets(input,Constant,stdin)!=NULL){        // Continuous loop to read input unless EOF
        
		command = input[0];                     // extract command from input

        switch(command){                        // check weather command is V,s,e and act accordingly

        case 'V':                               // if command = V
            sscanf(input,"V %d",&no_of_vertex);  // extract #of vertex from input
			fprintf(stdout,"V %d\n",no_of_vertex);
			fflush(stdout);
			initialize_graph(&Graph);
			add_vertex(no_of_vertex,&Graph);         // add vertex to graph
			break;

        case 'E':                               // if command = E
            e=0;
			i=0;
			//initialize_graph(&Graph);
            token=strtok(input,split);
             while (token){
                sscanf(token,"%d",&edges[e]);
				//edges[e]=edges[e]-1;
				//printf("%d, %d ",edges[e],e);
                token = strtok(NULL,split);
                e++;
                }

            for(i=0;i<e-1;i+=2){
                e1=edges[i];
                e2=edges[i+1];
                check = edge_exist_check(e1,e2,&Graph,'E');
                if(check==0){
                    break;
                }
            }
            if (i<e-1){
                initialize_graph(&Graph);
                continue;
            }

            else {
                add_edges(e-1,edges,&Graph);
                fprintf(stdout,"E {");
                for(i=0;i<e-1;i=i+2){
                    if(i<e-3){
                        fprintf(stdout,"<%d,%d>,",edges[i],edges[i+1]);
                    }else{
                        fprintf(stdout,"<%d,%d>",edges[i],edges[i+1]);
                    }
                }
                fprintf(stdout,"}\n");
                fflush(stdout);
            }
			
            break;

        case 's':                               // if command = s
            sscanf(input,"s %d %d",&point1,&point2);
            if (edge_exist_check(point1,point2,&Graph,'s')==0){
                continue;
                }
            else if (point1==point2){
                fprintf(stdout,"%d\n",point1);
                }
            else {
                shortest_path(point1,point2,&Graph);
                display_path(point1, point2, &Graph);
				fprintf(stdout,"\n");
                }
			fflush(stdout);
            break;

        default:
            break;
			
		

        }
		fflush(stdout);
    }

    return 0;

}