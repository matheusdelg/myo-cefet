#include "defs.h"
 
// auxiliares:
void drawScreen(float, float);
void createGL(void);
void openFile(void);
 
// Chamados no callbackDraw:
void drawGrid(float, float);
void drawPoints(void);
 
// Callback's do OpenGL:
void callback(void);
void callbackKeyboard(unsigned char, int, int);
 
// Variáveis globais:
int samples[SAMPLES], emg[8], countSamples = 0, sensor = 0;
short running = TRUE;
 
// Cores:
float red[8]   = {0,   0.25,  0.125, 0.625, 0.25, 1, 0.375, 0};
float green[8] = {0,   0.5,   0.5,   0.125, 0.25, 0, 0.375, 1};
float blue[8]  = {1,   0.25,  0.375, 0.25,  0.5,  0, 0.25,  0};
 
/** Inicializador do OpenGL:
**/
void createGL(void)
{
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB);
 
    glutInitWindowSize (SCREENX, SCREENY);
 
    glutCreateWindow (TITLE);
    glutDisplayFunc (callback);
    glutIdleFunc (callback);
    glutKeyboardFunc (callbackKeyboard);
 
    glClearColor WHITE;
    glMatrixMode (GL_PROJECTION);
    glLoadIdentity();
   
    gluOrtho2D (MINX, MAXX, MINY, MAXY);
    glMatrixMode (GL_MODELVIEW);
   
    FILE* pf = open DATAFILE;
    running = CHECK_RUN;
    fclose(pf);
}
 
/** Callback Idle:
    Função executada quando o programa está ocioso. Atualiza o vetor
    de amostras do EMG.
**/
void callback(void)
{
    // Lê e copia do arquivo:
    openFile();
 
    // Copia o valor do EMG selecionado para o
    // array de amostras:
   
    samples[countSamples] = emg[sensor];
 
    // Atualiza a quantidade máxima de amostras:
    countSamples = (++countSamples) % SAMPLES;
 
    // Chama a função de desenho:
    drawScreen(2, 2);
}
 
/** Loop principal:
        Desenha o fundo quadriculado em linhas cinzas espaçadas
        horizontalmente de x e vericalmente de y
        através da função drawGrid e chama a função drawPoints.
**/
void drawScreen(float x, float y)
{
    glClear(GL_COLOR_BUFFER_BIT);
 
    // Desenha na tela:
    drawGrid(x, y);
    drawPoints();
   
    // Manda para o monitor:   
    glutSwapBuffers();
    glutPostRedisplay();
}
 
 /** Callback do teclado:
        Faz a leitura do teclado através de key. Identifica
        a tecla através de um switch e realiza a função
        necessária dentro do bloco. Seta a variavel
        keyboardAvailable como FALSE, para que o loop
        principal seja executado.
 **/
void callbackKeyboard (unsigned char key, int x, int y)
{
    glutPostRedisplay();
    switch (key)
    {
        case ESC:
            exit(0); // Se apertado ESC, encerra o programa
        break;
 
        case ENTER:
            sensor = (sensor + 1) % 8; // Se apertado ENTER,
            countSamples = 0;      // entra no modo de
        break;                 // escolha do sensor
    }
}
 
/** Desenha Grade:
    Desenha retangulos de x * y na tela
    de (MAXX - MINX) * (MAXY - MINY):      
**/
void drawGrid(float x, float y)
{
   float iterator;
 
   // Cor como cinza e espessura de linha 1:
   glColor3f GRAY;
   glLineWidth(1);
 
   // Inicia o desenho das linhas horizontais:
   glBegin(GL_LINES);  
      for(iterator = MINY; iterator < MAXY; iterator += x)
      {
          glVertex2f(MINX, iterator);
          glVertex2f(MAXX, iterator);
      }
   glEnd();
 
   // Inicia o desenho das linhas verticais:
   glBegin(GL_LINES);  
      for(iterator = MINX; iterator < MAXX; iterator += y)
      {
          glVertex2f(iterator, MINY);
          glVertex2f(iterator, MAXY);
      }
   glEnd();
}
 
/** Desenha Pontos:
    Desenha cada valor do vetor de amostras espaçadas
    por SCALEX.
**/
void drawPoints (void)
{
    int iterator, x, y;
 
    // Espessura da linha em 1.5
    glLineWidth(1.5);
 
    // Seleciona a cor do sensor:
    glColor3f(red[sensor], green[sensor], blue[sensor]);
 
    // Inicia o desenho da linha:
    glBegin(GL_LINE_STRIP);
       x = MINX - 1;
       // Desenha cada valor de samples já preenchido:
       for (iterator = 0; iterator < countSamples; ++iterator)
       {
          y = samples[iterator]; x++;
          glVertex2f(x, y);
       }
    glEnd();
}
 
void openFile(void)
{
    FILE* pf = open DATAFILE;
    running = CHECK_RUN;
    fscanf(pf, "%d\n%d\n%d\n%d\n%d\n%d\n%d\n%d",
    &emg[0], &emg[1], &emg[2], &emg[3], &emg[4],
    &emg[5], &emg[6], &emg[7]);
    fclose(pf);
}
