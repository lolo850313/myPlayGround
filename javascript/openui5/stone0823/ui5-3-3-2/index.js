sap.ui.define([
    "sap/m/RadioButton",
    "sap/m/Label",
    "sap/m/RadioButtonGroup"
], function (RadioButton, Label, RadioButtonGroup) {
    "use strict";
    
    var btn1 = new RadioButton({
        text : "yes",
    })

    var btn2 = new RadioButton({
        text : "no",
    })

    var oLabel = new Label({
        text : "Do you like basketball?"
    }).placeAt("content")

    var oRadioBtnGrp = new RadioButtonGroup({
        columns : 2,
    }).placeAt("content")

    oRadioBtnGrp.addButton(btn1)
    oRadioBtnGrp.addButton(btn2)

})