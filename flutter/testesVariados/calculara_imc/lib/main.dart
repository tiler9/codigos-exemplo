import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    home: Home(),
  ));
}

class Home extends StatefulWidget {
  @override
  _HomeState createState() => _HomeState();
}

class _HomeState extends State<Home> {

  TextEditingController weightController = TextEditingController();
  TextEditingController heightController = TextEditingController();

  GlobalKey<FormState> _formKey = GlobalKey<FormState>();


  String _infoText = "Informe seus dados";

  void _resetFields(){

    //não precisa nos controladores
    weightController.text = "";
    heightController.text = "";

    setState(() {
      _infoText = "Informe seus dados";
      _formKey = GlobalKey<FormState>();
    });

  }

  void calculate(){
    setState(() {
      double weight = double.parse(weightController.text);
      double height = double.parse(heightController.text) / 100; // altura em metros
      double imc = (weight / (height * height));
      if(imc < 18.6){
        _infoText = "IMC calculado: ${imc.toStringAsPrecision(3)}. Abaixo do peso ideal para altura!";
      }else if(imc >= 18.6 && imc <= 24.9){
        _infoText = "IMC calculado: ${imc.toStringAsPrecision(3)}. Peso Ideal!";
      }else if(imc >= 24.9 && imc <= 29.9){
        _infoText = "IMC calculado: ${imc.toStringAsPrecision(3)}. Levemente acima do peso!";
      }else if(imc >= 29.9 && imc <= 34.9){
        _infoText = "IMC calculado: ${imc.toStringAsPrecision(3)}. Obesidade Grau I!";
      }else if(imc >= 34.9 && imc <= 39.9){
        _infoText = "IMC calculado: ${imc.toStringAsPrecision(3)}., Obesidade Grau II!";
      }else if(imc >= 40.0){
        _infoText = "IMC calculado: ${imc.toStringAsPrecision(3)}. Obesidade Grau III!";
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("Calculadora de IMC"),
          centerTitle: true,
          backgroundColor: Colors.green,
          actions: <Widget>[
            IconButton(
              icon: Icon(Icons.refresh),
              onPressed: _resetFields,
            )
          ],
        ),
        backgroundColor: Colors.white,
        body: SingleChildScrollView(
            padding: EdgeInsets.fromLTRB(10.0, 0.0, 10.0, 0.0),
            child: Form(
              key: _formKey,
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: <Widget>[
                  Icon(Icons.person, size: 120.0, color: Colors.green),
                  TextFormField(
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                        labelText: "Peso (kg):",
                        labelStyle: TextStyle(color: Colors.green)),
                    textAlign: TextAlign.center,
                    style: TextStyle(color: Colors.green, fontSize: 20.0),
                    controller: weightController,
                    validator: (value) {
                      if(value.isEmpty){
                        return "Insira seu Peso";
                      }
                      return null;
                    },
                  ), // Peso
                  TextFormField(
                    keyboardType: TextInputType.number,
                    decoration: InputDecoration(
                        labelText: "Altura (cm):",
                        labelStyle: TextStyle(color: Colors.green)),
                    textAlign: TextAlign.center,
                    style: TextStyle(color: Colors.green, fontSize: 20.0),
                    controller: heightController,
                    validator: (value) {
                      if(value.isEmpty){
                        return "Insira sua Altura";
                      }
                      return null;
                    },
                  ), //Altura
                  Container(
                    padding: EdgeInsets.fromLTRB(0.0, 10.0, 0.0, 10.0),
                    height: 80.0,
                    child: RaisedButton(
                      child: Text("Calcular",
                          style: TextStyle(color: Colors.white, fontSize: 20.0)),
                      onPressed: (){
                        if(_formKey.currentState.validate()){
                          calculate();
                        }
                      },
                      color: Colors.green,
                    ),
                  ), //botão de CALCULAR
                  Text(_infoText,
                      textAlign: TextAlign.center,
                      style: TextStyle(color: Colors.green, fontSize: 25.0)),
                ],
              )
            )
        ));
  }
}
