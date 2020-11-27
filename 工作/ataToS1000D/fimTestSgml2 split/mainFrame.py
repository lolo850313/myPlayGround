def frame(faultcodeARJ):
    from lxml import etree
    from lxml.builder import ElementMaker
    from subtask import subtask_merge    

    E = ElementMaker()
    #************************初始化相关E工厂对象，形成基本树（即不管arj项目如何构成，都需要的基本子元素）
    content_XML = E.content
    referencedApplicGroupRef_XML = E.referencedApplicGroupRef
    applicRef_XML = E.applicRef
    warningsAndCautionsRef_XML = E.warningsAndCautionsRef
    
    warningRef_XML = E.warningRef

    faultIsolation_XML = E.faultIsolation
    commonInfo_XML = E.commonInfo
    faultIsolationProcedure_XML = E.faultIsolationProcedure
    warningsAndCautionsRef_XML = E.warningsAndCautionsRef

    fault_XML = E.fault
    
    faultDescr_XML = E.faultDescr
    descr_XML = E.descr
    possibleCauseGroup_XML = E.possibleCauseGroup
    otherPossibleCause_XML = E.otherPossibleCause
    isolationProcedure_XML = E.isolationProcedure
    preliminaryRqmts_XML = E.preliminaryRqmts
    isolationMainProcedure_XML = E.isolationMainProcedure
    closeRqmts_XML = E.closeRqmts
    reqCondGroup_XML = E.reqCondGroup
    #无收尾操作则生成noConds标签
    noConds_XML = E.noConds

    reqCondCircuitBreaker_XML = E.reqCondCircuitBreaker
    reqCond_XML = E.reqCond
    circuitBreakerDescrGroup_XML = E.circuitBreakerDescrGroup
    circuitBreakerDescrSubGroup_XML = E.circuitBreakerDescrSubGroup
    circuitBreakerDescr_XML = E.circuitBreakerDescr
    circuitBreakerRef_XML = E.circuitBreakerRef
    name_XML = E.name
    reqSafety_XML = E.reqSafety
    reqSupportEquips_XML = E.reqSupportEquips
    noSupportEquips_XML = E.noSupportEquips

    reqSupplies_XML = E.reqSupplies
    noSupplies_XML = E.noSupplies

    reqSpares_XML = E.reqSpares
    noSpares_XML = E.noSpares

    noSupportEquips_XML = E.noSupportEquips
    noSupplies_XML = E.noSupplies
    noSpares_XML = E.noSpares
    #如果没有warning，caution呢？
    noSafety_XML = E.noSafety

    isolationProcedureEnd_XML = E.isolationProcedureEnd
    #初步评估
    circuitBreakerRef_XML = E.circuitBreakerRef
    randomList_XML = E.randomList
    listItem_XML = E.listItem
    title_XML = E.title
    dmRef_XML = E.dmRef
    dmRefIdent_XML = E.dmRefIdent
    dmCode_XML = E.dmCode
    sequentialList_XML = E.sequentialList
    para_XML = E.para
    reqCondNoRef_XML = E.reqCondNoRef
    reqCond_XML = E.reqCond
    # 有无warning caution
    # safetyRqmts_XML = E.safetyRqmts

    content_element = content_XML(
        faultIsolation_XML
            (commonInfo_XML,
            faultIsolationProcedure_XML
                # 故障代码
                (fault_XML(faultCode = faultcodeARJ),
                # 故障描述
                faultDescr_XML,
                possibleCauseGroup_XML,
                isolationProcedure_XML
                    (preliminaryRqmts_XML
                        (reqCondGroup_XML(noConds_XML),
                        reqSupportEquips_XML(noSupportEquips_XML),
                        reqSupplies_XML(noSupplies_XML),
                        reqSpares_XML(noSpares_XML),
                        reqSafety_XML(noSafety_XML)
                        ),
                    isolationMainProcedure_XML,
                    closeRqmts_XML
                        (reqCondGroup_XML
                            (reqCondNoRef_XML
                                (reqCond_XML("在故障隔离程序结束前，使飞机或系统恢复正常状态。"))
                            )
                        )    
                    )
                )
            )
        
    )

    return content_element





