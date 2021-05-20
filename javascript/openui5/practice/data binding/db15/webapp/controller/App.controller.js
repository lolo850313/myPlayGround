sap.ui.define([
    'sap/ui/core/mvc/Controller',
    'sap/m/library',
    'sap/ui/core/Locale',
    'sap/ui/core/LocaleData',
    "sap/ui/model/type/Currency",
    "sap/m/ObjectAttribute"
], function(Controller, mobileLibrary, Locale, LocaleData, Currency, ObjectAttribute) {
    'use strict';
    
    return Controller.extend("sap.ui.demo.db.controller.App", {
        formatMail : function (sFirstName, sLastName) {
            var oBundle = this.getView().getModel("i18n").getResourceBundle()

            return mobileLibrary.URLHelper.normalizeEmail(
                sFirstName + "." + sLastName + "@example.com",
                oBundle.getText("mailSubject", [sFirstName]),
                oBundle.getText("mailBody")
            )
        },

        formatStockValue : function (fUnitPrice, iStockLevel, sCurrCode) {
            var oCurrency = new Currency();
            return oCurrency.formatValue([fUnitPrice * iStockLevel, sCurrCode], "string")
        },

        onItemSelected : function (oEvent) {
            // 得到当前事件的dom元素
            var oSelectedItem = oEvent.getSource()
            // 得到当前dom元素的product上下文
            var oContext = oSelectedItem.getBindingContext("products")
            // 得到products的路径/Products/4
            var sPath = oContext.getPath()

            var oProductDetailPanel = this.byId("productDetailsPanel")

            oProductDetailPanel.bindElement({
                path : sPath,
                model : "products"
            })
        },
        productListFactory : function (sId, oContext) {
            console.log(sId);
            console.log(oContext);
            var oUIControl;

            if (oContext.getProperty("UnitsInStock") === 0 && oContext.getProperty("Discontinued")) {
                oUIControl = this.byId("productSimple").clone(sId)
                console.log(111);
                console.log(oUIControl);
                console.log(this.byId("productSimple"));
            } else {
                oUIControl = this.byId("productExtended").clone(sId)
                if (oContext.getProperty("UnitsInStock") < 1) {
                    oUIControl.addAttribute(new ObjectAttribute({
                        text : {
                            path : "i18n>outOfStock"
                        }
                    }))
                    console.log(222);
                    console.log(oUIControl);
                    console.log(this.byId("productSimple"));
                }
            }

            return oUIControl
        }
    })
});