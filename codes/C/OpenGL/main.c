#include <stdlib.h>
#include <stdio.h>

#include <GL/glut.h> // para OpenGL

#include "grafico.h" // funções aqui

// Função Principal:
int main (int argc, char** argv){
    // Essencial para linux
    glutInit(&argc, argv);
    // Inicializa todas as condições
    createGL();

    // Inicia loop principal:
    while(running)
        glutMainLoopEvent();
}
