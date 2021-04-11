sap.ui.define([
    'sap/ui/core/UIComponent',
    'sap/ui/model/json/JSONModel',
    'sap/ui/model/resource/ResourceModel',

], function(UIComponent, JSONModel, ResourceModel) {
    "use strict";

    return UIComponent.extend("sap.ui.demo.walkthrough.Component", {
        metadata : {
            rootView : {
                "viewName" : "sap.ui.demo.walkthrough.view.App",
                "type" : "XML",
                "async" : true,
                "id" : "app"
            }
        },

        init : function () {
            UIComponent.prototype.init.apply(this, arguments)

            var oData = {
                recipient:{
                    name :"UI 5 uicomponent"
                }
            }

            var oModel = new JSONModel(oData)
            this.getView().setModel(oModel)

            var i18nModel = new ResourceModel({
                bundelName : "sap.ui.demo.walkthrough.i18n.i18n",
                supportedLocales:[""],
                fallbackLocale:""
            })

            this.getView().setModel(i18nModel, "i18n")

            
        }

    })
});