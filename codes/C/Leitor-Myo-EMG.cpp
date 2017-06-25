#include <myo/myo.hpp>
#include <array>
#include <iostream>
#include <fstream>
#include <string>

class MyoEMG : public myo::DeviceListener {
public:

	// Array de dados do EMG:
	std::array<float, 8> emgSamples;
	// Hub para Myo:
	myo::Hub* hub;

	// Construtor vazio:
	MyoEMG () : emgSamples () {}

	// Chamado quando o Myo é desconectado:
	void onUnpair (myo::Myo* myo, uint64_t timestamp);
	// Chamado a cada atualização do EMG (200Hz):
    void onEmgData (myo::Myo* myo, uint64_t timestamp, const int8_t* emg);
    // Escrever no arquivo de saída:
    void updateFile (std::string fname);
    // Conecta ao Myo (retorna nullptr caso contrário):
    myo::Myo* connect (uint32_t timeout, std::string appname);
};

myo::Myo* MyoEMG::connect (uint32_t timeout, std::string appname){

	hub = new myo::Hub(appname);
	myo::Myo* device = hub->waitForMyo(timeout);

	if(!device) return nullptr;

	device->setStreamEmg(myo::Myo::streamEmgEnabled);
	return device;
}

void MyoEMG::onUnpair (myo::Myo* myo, uint64_t timestamp){
	std::cout << "Conexão com o Myo perdida! " << std::endl;
	// Zerando o array para evitar dados incorretos
	emgSamples.fill(0);
}

void MyoEMG::onEmgData (myo::Myo* myo, uint64_t timestamp, const int8_t* emg){
	// Copia valores do EMG para o array da classe
	for (int i = 0; i < 8; ++i)
		emgSamples[i] = emg[i];
}

void MyoEMG::updateFile (std::string fname) {
	std::cout << "\r";

	// Abre arquivo
	std::ofstream myoemg;
	myoemg.open(fname + ".emg");

	// Copia informações
	for(size_t i = 0; i < this->emgSamples.size(); ++i){
		myoemg << static_cast <float> (this->emgSamples[i]) << std::endl;
	}

	// Fecha arquivo
	myoemg.close();
}

#define TIMEOUT 3000
#define FREQ  50
#define mainLoop while(1)

// Programa principal:
int main (int argc, char** argv){
try {
	// Inicia um coletor:
	MyoEMG emg;
	// Inicia conexão com dispositivo:
	myo::Myo* dispositivo = emg.connect(TIMEOUT, "cefet.ger.myo.teste.myoemg");

	// Caso não encontrado:
	if(dispositivo == nullptr){
		std::cout << "Myo não encontrado! " << std::endl;
		std::cerr << "Aperte qualquer tecla para encerrar";
		std::cin.ignore();
		return -1;
	}

	// Associa os listeners "onUpdate" e "onEmgData" da classe:
	emg.hub->addListener(&emg);

	// Loop principal (50Hz):
	mainLoop {
		emg.hub->run(FREQ);
		emg.updateFile("myo.emg");
	}

// Caso alguma exceção genérica seja lançada (como memória
// insuficiente ou "Myo Connect" não funcionando):
}catch (std::exception& e){
	std::cerr << "Erro! " << e.what() << std::endl;
	std::cin.ignore();
	return -1;
}
}
