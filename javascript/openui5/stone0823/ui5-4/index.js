sap.ui.define([
    "sap/m/Image",
    "sap/m/Label",
    "sap/m/RadioButtonGroup",
    "sap/m/RadioButton"
], function (Image, Label, RadioButton, RadioButtonGroup) {
    "use strict";
    
    var oImage1 = new Image({
        src : "img/donghai.jpg",
        decorative: false,
        alt: 'donghai'
    }).placeAt("content")

    var oImage2 = new Image({
        src : "img/adi.jpg",
        decorative: false,
        alt: 'adi'
    }).placeAt("content")

    var btn1 = new RadioButton({
        text : "left logo",
    })

    var btn2 = new RadioButton({
        text : "right logo",
    })

    var oLabel1 = new Label({
        text : "Which logo do you like better?"
    })

    var oRadioBtnGrp1 = new RadioButtonGroup({
        columns : 2,
        ariaLabelledBy: oLabel1,
        buttons:[
            btn1,
            btn2
        ]
    }).placeAt("content")

})