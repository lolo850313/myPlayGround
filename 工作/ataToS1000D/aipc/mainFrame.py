def frame(arjTitle,graphicId):
    from lxml import etree
    from lxml.builder import ElementMaker  

    E = ElementMaker()
    #************************初始化相关E工厂对象，形成基本树（即不管arj项目如何构成，都需要的基本子元素）
    content_XML = E.content
    illustratedPartsCatalog_XML = E.illustratedPartsCatalog
    figure_XML = E.figure    
    title_XML = E.title    

    content_element = content_XML(
        illustratedPartsCatalog_XML
            (figure_XML(
                title_XML(arjTitle),
                id=graphicId
            )
        )        
    )

    return content_element





