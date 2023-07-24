#include <stdio.h>
#include <stdint.h>

void main(){
	
	uint8_t dhAtual[] = {30,4,4,23,50}, dhLib[] = {0,0,0,0,0}, bloqueio = 10;
	
	uint8_t isBissexto = 0, isMes31 = 0;
	uint8_t mesesCom31Dias[] = {1,3,5,7,8,10,12};

	
	
	printf("\ndhAtual: %d/%d/%d - %dh:%dmin", dhAtual[0],dhAtual[1],dhAtual[2],dhAtual[3],dhAtual[4]);

	//======= MINUTOS
	dhLib[4] = dhAtual[4] + bloqueio;
	
	dhLib[4] -= (dhLib[4]/60)*60;
	
	//====== HORAS
	dhLib[3] = dhAtual[3] ;
	
	if((dhAtual[4] + bloqueio)/60 > 0) 
		dhLib[3]++;
	
	if(dhLib[3] == 24){
		dhLib[3] = 0;
		dhLib[0]++;
	}
	
	//====== DIA
	dhLib[2] = dhAtual[2] ;
	dhLib[1] = dhAtual[1] ;
	dhLib[0] += dhAtual[0] ;
	
	uint8_t i = 0;
	for( i = 0; i < sizeof(mesesCom31Dias) ; i++ ){
		if(dhLib[1] == mesesCom31Dias[i])
			isMes31 = 1;
	}
		
			
	if(isMes31 == 1){ // meses com nº de dias 31
		if(dhLib[0] > 31){
			dhLib[0] = 1;
			dhLib[1]++;
		}
	}else if(dhLib[1] == 2){ //mês de fevereiro
		if ( ( dhLib[2] % 4 == 0 && dhLib[2] % 100 != 0 ) || dhLib[2] % 400 == 0 ){ //checando se o ano é bissexto
			if(dhLib[0] > 29){
				dhLib[0] = 1;
				dhLib[1]++;
			}
		}else{
			if(dhLib[0] > 28){
				dhLib[0] = 1;
				dhLib[1]++;
			}
		}
    		
	}else{ // meses com nº de dias 30
		if(dhLib[0] > 30){
			dhLib[0] = 1;
			dhLib[1]++;
		}
	}
			
	//====== MÊS
	if(dhLib[1] > 12){
		dhLib[1] = 1;
		dhLib[2]++;
	}
	
	//====== ANO
	if(dhLib[2] > 99)
		dhLib[2] = 0;
	
	
	
	printf("\ndhLib: %d/%d/%d - %dh:%dmin", dhLib[0],dhLib[1],dhLib[2],dhLib[3],dhLib[4]);
	
		
}
