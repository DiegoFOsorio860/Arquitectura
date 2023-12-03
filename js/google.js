function myFunction() {

    const hoja_arquitectura = SpreadsheetApp.getActiveSpreadsheet();
    const arquitectura = hoja_arquitectura.getSheetByName('ARQUITECTURA');
  
    const f1_1 = arquitectura.getRange('E10').getValue();
    const f1_2 = arquitectura.getRange('F10').getValue();
    const f1_3 = arquitectura.getRange('G10').getValue();
  
    const t1_1 = arquitectura.getRange('E11').getValue();
    const t1_2 = arquitectura.getRange('F11').getValue();
  
    const op1_1 = arquitectura.getRange('E12').getValue();
    const op1_2 = arquitectura.getRange('F12').getValue();
    const op1_3 = arquitectura.getRange('G12').getValue();
  
    const ap1_1 = arquitectura.getRange('E13').getValue();
    const ap1_2 = arquitectura.getRange('F13').getValue();
    const ap1_3 = arquitectura.getRange('G13').getValue();
    
    const aa01_1 = arquitectura.getRange('E14').getValue();
    const aa01_2 = arquitectura.getRange('F14').getValue();
    const aa01_3 = arquitectura.getRange('G14').getValue();
  
    const pta_1_1 = arquitectura.getRange('E15').getValue();
    const pta_1_2 = arquitectura.getRange('F15').getValue();
    const pta_1_3 = arquitectura.getRange('G15').getValue();
  
      // ====================================================================
    const htmlTemplate = HtmlService.createTemplateFromFile('guia_aprend_1');
    // ====================================================================

    // Fase
  htmlTemplate.f1_1 = f1_1;
  htmlTemplate.f1_2 = f1_2;
  htmlTemplate.f1_3 = f1_3;

  //Trimestre
  htmlTemplate.t1_1 = t1_1;
  htmlTemplate.t1_2 = t1_2;

  // Objetivo de Proyecto
  htmlTemplate.op1_1 = op1_1;
  htmlTemplate.op1_2 = op1_2;
  htmlTemplate.op1_3 = op1_3;

  // Actividad de Proyecto
  htmlTemplate.ap1_1 = ap1_1;
  htmlTemplate.ap1_2 = ap1_2;
  htmlTemplate.ap1_3 = ap1_3;

  // Actividad de Aprendizaje
  htmlTemplate.aa01_1 = aa01_1;
  htmlTemplate.aa01_2 = aa01_2;
  htmlTemplate.aa01_3 = aa01_3;

  // Producto de Trabajo del Aprendiz
  htmlTemplate.pta_1_1 = pta_1_1;
  htmlTemplate.pta_1_2 = pta_1_2;
  htmlTemplate.pta_1_3 = pta_1_3;

  // ============================================================================

  const cod_1_1 = 'Código Competencia'
  const cod_1_2 = 'Descripción Competencia'
  const cod_1_3 = 'F.Directa'
  const cod_1_4 = 'F.Autónoma'

  htmlTemplate.cod_1_1 = cod_1_1;
  htmlTemplate.cod_1_2 = cod_1_2;
  htmlTemplate.cod_1_3 = cod_1_3;
  htmlTemplate.cod_1_4 = cod_1_4;

  // ====================================================================
    // ETIQUETAS

  // Etiquetas
  const cod_rap_1_1 = 'Código Resultado'
  const cod_rap_1_2 = 'Descripción Resultado'
  const cod_rap_1_3 = 'F.Directa'
  const cod_rap_1_4 = 'F.Autónoma'

  htmlTemplate.cod_rap_1_1 = cod_rap_1_1;
  htmlTemplate.cod_rap_1_2 = cod_rap_1_2;
  htmlTemplate.cod_rap_1_3 = cod_rap_1_3;
  htmlTemplate.cod_rap_1_4 = cod_rap_1_4;

    // Etiquetas
  const cod_clas_1_1 = 'Código Clasificación Competencia'
  const cod_clas_1_2 = 'Descripción Clasificación Competencia'
  const cod_clas_1_3 = 'F.Directa'
  const cod_clas_1_4 = 'F.Autónoma'

  htmlTemplate.cod_clas_1_1 = cod_clas_1_1;
  htmlTemplate.cod_clas_1_2 = cod_clas_1_2;
  htmlTemplate.cod_clas_1_3 = cod_clas_1_3;
  htmlTemplate.cod_clas_1_4 = cod_clas_1_4;

  const cod_con_1_1 = 'Código Conocimiento'
  const cod_con_1_2 = 'Descripción Conocimiento'
  const cod_con_1_3 = 'F.Directa'
  const cod_con_1_4 = 'F.Autónoma'

  htmlTemplate.cod_con_1_1 = cod_con_1_1;
  htmlTemplate.cod_con_1_2 = cod_con_1_2;
  htmlTemplate.cod_con_1_3 = cod_con_1_3;
  htmlTemplate.cod_con_1_4 = cod_con_1_4;

  // Competencia Hidraulica

  const comp_codigo_E16 = arquitectura.getRange('E16').getValue();
  const comp_descrip_F16 = arquitectura.getRange('F16').getValue();

  const rap_codigo_E17 = arquitectura.getRange('E17').getValue();
  const rap_descrip_F17 = arquitectura.getRange('F17').getValue();

  const clas_E18 = arquitectura.getRange('E18').getValue();
  const clas_F18 = arquitectura.getRange('F18').getValue();

  htmlTemplate.clas_E18 = clas_E18;
  htmlTemplate.clas_F18 = clas_F18;

  const cono_E19 = arquitectura.getRange('E19').getValue();
  const cono_G19 = arquitectura.getRange('G19').getValue();
  const cono_M19 = arquitectura.getRange('M19').getValue();
  const cono_N19 = arquitectura.getRange('N19').getValue();

  const cono_E20 = arquitectura.getRange('E20').getValue();
  const cono_G20 = arquitectura.getRange('G20').getValue();
  const cono_M20 = arquitectura.getRange('M20').getValue();
  const cono_N20 = arquitectura.getRange('N20').getValue();

  const cono_E21 = arquitectura.getRange('E21').getValue();
  const cono_G21 = arquitectura.getRange('G21').getValue();
  const cono_M21 = arquitectura.getRange('M21').getValue();
  const cono_N21 = arquitectura.getRange('N21').getValue();

  const cono_E22 = arquitectura.getRange('E22').getValue();
  const cono_G22 = arquitectura.getRange('G22').getValue();
  const cono_M22 = arquitectura.getRange('M22').getValue();
  const cono_N22 = arquitectura.getRange('N22').getValue();

  const cono_E23 = arquitectura.getRange('E23').getValue();
  const cono_G23 = arquitectura.getRange('G23').getValue();
  const cono_M23 = arquitectura.getRange('M23').getValue();
  const cono_N23 = arquitectura.getRange('N23').getValue();

  const cono_E24 = arquitectura.getRange('E24').getValue();
  const cono_G24 = arquitectura.getRange('G24').getValue();
  const cono_M24 = arquitectura.getRange('M24').getValue();
  const cono_N24 = arquitectura.getRange('N24').getValue();

  const cono_E25 = arquitectura.getRange('E25').getValue();
  const cono_G25 = arquitectura.getRange('G25').getValue();
  const cono_M25 = arquitectura.getRange('M25').getValue();
  const cono_N25 = arquitectura.getRange('N25').getValue();

  const cono_E26 = arquitectura.getRange('E26').getValue();
  const cono_G26 = arquitectura.getRange('G26').getValue();
  const cono_M26 = arquitectura.getRange('M26').getValue();
  const cono_N26 = arquitectura.getRange('N26').getValue();

  const cono_E27 = arquitectura.getRange('E27').getValue();
  const cono_G27 = arquitectura.getRange('G27').getValue();
  const cono_M27 = arquitectura.getRange('M27').getValue();
  const cono_N27 = arquitectura.getRange('N27').getValue();

  const cono_E28 = arquitectura.getRange('E28').getValue();
  const cono_G28 = arquitectura.getRange('G28').getValue();
  const cono_M28 = arquitectura.getRange('M28').getValue();
  const cono_N28 = arquitectura.getRange('N28').getValue();

  const evid_rot_1_1 = 'Código Evidencia'
  const evid_rot_1_2 = 'Descripción Evidencia'
  const evid_rot_1_3 = 'F.Directa'
  const evid_rot_1_4 = 'F.Autónoma'

  const evid_E29 = arquitectura.getRange('E29').getValue();
  const evid_G29 = arquitectura.getRange('G29').getValue();
  const evid_M29 = arquitectura.getRange('M29').getValue();
  const evid_N29 = arquitectura.getRange('N29').getValue();

  const evid_E30 = arquitectura.getRange('E30').getValue();
  const evid_G30 = arquitectura.getRange('G30').getValue();
  const evid_M30 = arquitectura.getRange('M30').getValue();
  const evid_N30 = arquitectura.getRange('N30').getValue();

  const evid_E31 = arquitectura.getRange('E31').getValue();
  const evid_G31 = arquitectura.getRange('G31').getValue();
  const evid_M31 = arquitectura.getRange('M31').getValue();
  const evid_N31 = arquitectura.getRange('N31').getValue();

  const evid_E32 = arquitectura.getRange('E32').getValue();
  const evid_G32 = arquitectura.getRange('G32').getValue();
  const evid_M32 = arquitectura.getRange('M32').getValue();
  const evid_N32 = arquitectura.getRange('N32').getValue();

  const evid_E33 = arquitectura.getRange('E33').getValue();
  const evid_G33 = arquitectura.getRange('G33').getValue();
  const evid_M33 = arquitectura.getRange('M33').getValue();
  const evid_N33 = arquitectura.getRange('N33').getValue();

  const sum_E34 = arquitectura.getRange('E34').getValue();
  const sum_G34 = arquitectura.getRange('G34').getValue();
  const sum_M34 = arquitectura.getRange('M34').getValue();
  const sum_N34 = arquitectura.getRange('N34').getValue();

  const tablaRango34 = arquitectura.getRange(7,4, 34, 11).getValues();

  const lineaTotal34 = arquitectura.getRange(34, 4,1,11).getValues();
  const totalSum34 = lineaTotal34[0][1];

  // HIDRAULICA
  // Competencia
  htmlTemplate.comp_codigo_E16 = comp_codigo_E16;
  htmlTemplate.comp_descrip_F16 = comp_descrip_F16;

  // Resultado de Aprendizaje 
  htmlTemplate.rap_codigo_E17 = rap_codigo_E17;
  htmlTemplate.rap_descrip_F17 = rap_descrip_F17;

  // Etiquetas

    // Conocimiento No 1
  htmlTemplate.cono_E19 = cono_E19;
  htmlTemplate.cono_G19 = cono_G19;
  htmlTemplate.cono_M19 = cono_M19;
  htmlTemplate.cono_N19 = cono_N19;

  // Conocimiento No 1
  htmlTemplate.cono_E20 = cono_E20;
  htmlTemplate.cono_G20 = cono_G20;
  htmlTemplate.cono_M20 = cono_M20;
  htmlTemplate.cono_N20 = cono_N20;

  // Conocimiento No 2
  htmlTemplate.cono_E21 = cono_E21;
  htmlTemplate.cono_G21 = cono_G21;
  htmlTemplate.cono_M21 = cono_M21;
  htmlTemplate.cono_N21 = cono_N21;

    // Conocimiento No 3
  htmlTemplate.cono_E22 = cono_E22;
  htmlTemplate.cono_G22 = cono_G22;
  htmlTemplate.cono_M22 = cono_M22;
  htmlTemplate.cono_N22 = cono_N22;

      // Conocimiento No 4
  htmlTemplate.cono_E23 = cono_E23;
  htmlTemplate.cono_G23 = cono_G23;
  htmlTemplate.cono_M23 = cono_M23;
  htmlTemplate.cono_N23 = cono_N23;

  // Conocimiento No 5
  htmlTemplate.cono_E23 = cono_E23;
  htmlTemplate.cono_G23 = cono_G23;
  htmlTemplate.cono_M23 = cono_M23;
  htmlTemplate.cono_N23 = cono_N23;

  // Conocimiento No 6
  htmlTemplate.cono_E24 = cono_E24;
  htmlTemplate.cono_G24 = cono_G24;
  htmlTemplate.cono_M24 = cono_M24;
  htmlTemplate.cono_N24 = cono_N24;

  // Conocimiento No 7
  htmlTemplate.cono_E25 = cono_E25;
  htmlTemplate.cono_G25 = cono_G25;
  htmlTemplate.cono_M25 = cono_M25;
  htmlTemplate.cono_N25 = cono_N25;

    // Conocimiento No 8
  htmlTemplate.cono_E26 = cono_E26;
  htmlTemplate.cono_G26 = cono_G26;
  htmlTemplate.cono_M26 = cono_M26;
  htmlTemplate.cono_N26 = cono_N26;

      // Conocimiento No 9
  htmlTemplate.cono_E27 = cono_E27;
  htmlTemplate.cono_G27 = cono_G27;
  htmlTemplate.cono_M27 = cono_M27;
  htmlTemplate.cono_N27 = cono_N27;

        // Conocimiento No 10
  htmlTemplate.cono_E28 = cono_E28;
  htmlTemplate.cono_G28 = cono_G28;
  htmlTemplate.cono_M28 = cono_M28;
  htmlTemplate.cono_N28 = cono_N28;

        // Evidencia Rotulo
  htmlTemplate.evid_rot_1_1 = evid_rot_1_1;
  htmlTemplate.evid_rot_1_2 = evid_rot_1_2;
  htmlTemplate.evid_rot_1_3 = evid_rot_1_3;
  htmlTemplate.evid_rot_1_4 = evid_rot_1_4;
  
// Evidencia No 1
  htmlTemplate.evid_E29 = evid_E29;
  htmlTemplate.evid_G29 = evid_G29;
  htmlTemplate.evid_M29 = evid_M29;
  htmlTemplate.evid_N29 = evid_N29;

// Evidencia No 1
  htmlTemplate.evid_E30 = evid_E30;
  htmlTemplate.evid_G30 = evid_G30;
  htmlTemplate.evid_M30 = evid_M30;
  htmlTemplate.evid_N30 = evid_N30;

  // Evidencia No 2
  htmlTemplate.evid_E31 = evid_E31;
  htmlTemplate.evid_G31 = evid_G31;
  htmlTemplate.evid_M31 = evid_M31;
  htmlTemplate.evid_N31 = evid_N31;

    // Evidencia No 3
  htmlTemplate.evid_E32 = evid_E32;
  htmlTemplate.evid_G32 = evid_G32;
  htmlTemplate.evid_M32 = evid_M32;
  htmlTemplate.evid_N32 = evid_N32;

      // Evidencia No 4
  htmlTemplate.evid_E33 = evid_E33;
  htmlTemplate.evid_G33 = evid_G33;
  htmlTemplate.evid_M33 = evid_M33;
  htmlTemplate.evid_N33 = evid_N33;


// Suma
  htmlTemplate.sum_E34 = sum_E34;
  htmlTemplate.sum_G34 = sum_G34;
  htmlTemplate.sum_M34 = sum_M34;
  htmlTemplate.sum_N34 = sum_N34;


  htmlTemplate.totalSum34 = totalSum34;
  htmlTemplate.tablaRango34 = tablaRango34;

// =========================================================================================================
  // RECOLECCION DE MUESTRAS

  const comp_codigo_E44 = arquitectura.getRange('E44').getValue();
  const comp_descrip_F44 = arquitectura.getRange('F44').getValue();

  const rap_codigo_E45 = arquitectura.getRange('E45').getValue();
  const rap_descrip_F45 = arquitectura.getRange('F45').getValue();

  // Competencia
  htmlTemplate.comp_codigo_E44 = comp_codigo_E44;
  htmlTemplate.comp_descrip_F44 = comp_descrip_F44;

  // Resultado de Aprendizaje 
  htmlTemplate.rap_codigo_E45 = rap_codigo_E45;
  htmlTemplate.rap_descrip_F45 = rap_descrip_F45;

  const clas_E46 = arquitectura.getRange('E46').getValue();
  const clas_F46 = arquitectura.getRange('F46').getValue();

  htmlTemplate.clas_E46 = clas_E46;
  htmlTemplate.clas_F46 = clas_F46;

  const cono_E47 = arquitectura.getRange('E47').getValue();
  const cono_G47 = arquitectura.getRange('G47').getValue();
  const cono_M47 = arquitectura.getRange('M47').getValue();
  const cono_N47 = arquitectura.getRange('N47').getValue();

  const cono_E48 = arquitectura.getRange('E48').getValue();
  const cono_G48 = arquitectura.getRange('G48').getValue();
  const cono_M48 = arquitectura.getRange('M48').getValue();
  const cono_N48 = arquitectura.getRange('N48').getValue();

  const cono_E49 = arquitectura.getRange('E49').getValue();
  const cono_G49 = arquitectura.getRange('G49').getValue();
  const cono_M49 = arquitectura.getRange('M49').getValue();
  const cono_N49 = arquitectura.getRange('N49').getValue();

  const cono_E50 = arquitectura.getRange('E50').getValue();
  const cono_G50 = arquitectura.getRange('G50').getValue();
  const cono_M50 = arquitectura.getRange('M50').getValue();
  const cono_N50 = arquitectura.getRange('N50').getValue();

  const cono_E51 = arquitectura.getRange('E51').getValue();
  const cono_G51 = arquitectura.getRange('G51').getValue();
  const cono_M51 = arquitectura.getRange('M51').getValue();
  const cono_N51 = arquitectura.getRange('N51').getValue();

  const cono_E52 = arquitectura.getRange('E52').getValue();
  const cono_G52 = arquitectura.getRange('G52').getValue();
  const cono_M52 = arquitectura.getRange('M52').getValue();
  const cono_N52 = arquitectura.getRange('N52').getValue();

  const cono_E53 = arquitectura.getRange('E53').getValue();
  const cono_G53 = arquitectura.getRange('G53').getValue();
  const cono_M53 = arquitectura.getRange('M53').getValue();
  const cono_N53 = arquitectura.getRange('N53').getValue();

  const cono_E54 = arquitectura.getRange('E54').getValue();
  const cono_G54 = arquitectura.getRange('G54').getValue();
  const cono_M54 = arquitectura.getRange('M54').getValue();
  const cono_N54 = arquitectura.getRange('N54').getValue();

  const cono_E55 = arquitectura.getRange('E55').getValue();
  const cono_G55 = arquitectura.getRange('G55').getValue();
  const cono_M55 = arquitectura.getRange('M55').getValue();
  const cono_N55 = arquitectura.getRange('N55').getValue();

  const cono_E56 = arquitectura.getRange('E56').getValue();
  const cono_G56 = arquitectura.getRange('G56').getValue();
  const cono_M56 = arquitectura.getRange('M56').getValue();
  const cono_N56 = arquitectura.getRange('N56').getValue();

  const evid_E57 = arquitectura.getRange('E57').getValue();
  const evid_G57 = arquitectura.getRange('G57').getValue();
  const evid_M57 = arquitectura.getRange('M57').getValue();
  const evid_N57 = arquitectura.getRange('N57').getValue();

  const evid_E58 = arquitectura.getRange('E58').getValue();
  const evid_G58 = arquitectura.getRange('G58').getValue();
  const evid_M58 = arquitectura.getRange('M58').getValue();
  const evid_N58 = arquitectura.getRange('N58').getValue();

  const evid_E59 = arquitectura.getRange('E59').getValue();
  const evid_G59 = arquitectura.getRange('G59').getValue();
  const evid_M59 = arquitectura.getRange('M59').getValue();
  const evid_N59 = arquitectura.getRange('N59').getValue();

  const evid_E60 = arquitectura.getRange('E60').getValue();
  const evid_G60 = arquitectura.getRange('G60').getValue();
  const evid_M60 = arquitectura.getRange('M60').getValue();
  const evid_N60 = arquitectura.getRange('N60').getValue();

  const evid_E61 = arquitectura.getRange('E61').getValue();
  const evid_G61 = arquitectura.getRange('G61').getValue();
  const evid_M61 = arquitectura.getRange('M61').getValue();
  const evid_N61 = arquitectura.getRange('N61').getValue();

  const sum_E62 = arquitectura.getRange('E62').getValue();
  const sum_G62 = arquitectura.getRange('G62').getValue();
  const sum_M62 = arquitectura.getRange('M62').getValue();
  const sum_N62 = arquitectura.getRange('N62').getValue();

  const tablaRango62 = arquitectura.getRange(7,4, 62, 11).getValues();

  const lineaTotal62 = arquitectura.getRange(62, 4,1,11).getValues();
  const totalSum62 = lineaTotal62[0][1];

  // Etiquetas

  htmlTemplate.cono_E47 = cono_E47;
  htmlTemplate.cono_G47 = cono_G47;
  htmlTemplate.cono_M47 = cono_M47;
  htmlTemplate.cono_N47 = cono_N47;

  // Conocimiento No 1
  htmlTemplate.cono_E48 = cono_E48;
  htmlTemplate.cono_G48 = cono_G48;
  htmlTemplate.cono_M48 = cono_M48;
  htmlTemplate.cono_N48 = cono_N48;

  // Conocimiento No 2
  htmlTemplate.cono_E49 = cono_E49;
  htmlTemplate.cono_G49 = cono_G49;
  htmlTemplate.cono_M49 = cono_M49;
  htmlTemplate.cono_N49 = cono_N49;

    // Conocimiento No 3
  htmlTemplate.cono_E50 = cono_E50;
  htmlTemplate.cono_G50 = cono_G50;
  htmlTemplate.cono_M50 = cono_M50;
  htmlTemplate.cono_N50 = cono_N50;

      // Conocimiento No 4
  htmlTemplate.cono_E51 = cono_E51;
  htmlTemplate.cono_G51 = cono_G51;
  htmlTemplate.cono_M51 = cono_M51;
  htmlTemplate.cono_N51 = cono_N51;

  // Conocimiento No 5
  htmlTemplate.cono_E52 = cono_E52;
  htmlTemplate.cono_G52 = cono_G52;
  htmlTemplate.cono_M52 = cono_M52;
  htmlTemplate.cono_N52 = cono_N52;

  // Conocimiento No 6
  htmlTemplate.cono_E53 = cono_E53;
  htmlTemplate.cono_G53 = cono_G53;
  htmlTemplate.cono_M53 = cono_M53;
  htmlTemplate.cono_N53 = cono_N53;

  // Conocimiento No 7
  htmlTemplate.cono_E54 = cono_E54;
  htmlTemplate.cono_G54 = cono_G54;
  htmlTemplate.cono_M54 = cono_M54;
  htmlTemplate.cono_N54 = cono_N54;

    // Conocimiento No 7
  htmlTemplate.cono_E55 = cono_E55;
  htmlTemplate.cono_G55 = cono_G55;
  htmlTemplate.cono_M55 = cono_M55;
  htmlTemplate.cono_N55 = cono_N55;

    // Conocimiento No 8
  htmlTemplate.cono_E56 = cono_E56;
  htmlTemplate.cono_G56 = cono_G56;
  htmlTemplate.cono_M56 = cono_M56;
  htmlTemplate.cono_N56 = cono_N56;

        // Evidencia Rotulo
  
  htmlTemplate.evid_E57 = evid_E57;
  htmlTemplate.evid_G57 = evid_G57;
  htmlTemplate.evid_M57 = evid_M57;
  htmlTemplate.evid_N57 = evid_N57;

// Evidencia No 1
  htmlTemplate.evid_E58 = evid_E58;
  htmlTemplate.evid_G58 = evid_G58;
  htmlTemplate.evid_M58 = evid_M58;
  htmlTemplate.evid_N58 = evid_N58;

  // Evidencia No 2
  htmlTemplate.evid_E59 = evid_E59;
  htmlTemplate.evid_G59 = evid_G59;
  htmlTemplate.evid_M59 = evid_M59;
  htmlTemplate.evid_N59 = evid_N59;

    // Evidencia No 3
  htmlTemplate.evid_E60 = evid_E60;
  htmlTemplate.evid_G60 = evid_G60;
  htmlTemplate.evid_M60 = evid_M60;
  htmlTemplate.evid_N60 = evid_N60;

      // Evidencia No 4
  htmlTemplate.evid_E61 = evid_E61;
  htmlTemplate.evid_G61 = evid_G61;
  htmlTemplate.evid_M61 = evid_M61;
  htmlTemplate.evid_N61 = evid_N61;

// Suma
  htmlTemplate.sum_E62 = sum_E62;
  htmlTemplate.sum_G62 = sum_G62;
  htmlTemplate.sum_M62 = sum_M62;
  htmlTemplate.sum_N62 = sum_N62;

  htmlTemplate.totalSum62 = totalSum62;
  htmlTemplate.tablaRango62 = tablaRango62

  // =========================================================================================================
  // INGLES

  const comp_codigo_E309 = arquitectura.getRange('E309').getValue();
  const comp_descrip_F309 = arquitectura.getRange('F309').getValue();

  const rap_codigo_E310 = arquitectura.getRange('E310').getValue();
  const rap_descrip_F310 = arquitectura.getRange('F310').getValue();

  // Competencia
  htmlTemplate.comp_codigo_E309 = comp_codigo_E309;
  htmlTemplate.comp_descrip_F309 = comp_descrip_F309;

  // Resultado de Aprendizaje 
  htmlTemplate.rap_codigo_E310 = rap_codigo_E310;
  htmlTemplate.rap_descrip_F310 = rap_descrip_F310;

  const clas_E311 = arquitectura.getRange('E311').getValue();
  const clas_F311 = arquitectura.getRange('F311').getValue();

  htmlTemplate.clas_E311 = clas_E311;
  htmlTemplate.clas_F311 = clas_F311;

  const cono_E312 = arquitectura.getRange('E312').getValue();
  const cono_G312 = arquitectura.getRange('G312').getValue();
  const cono_M312 = arquitectura.getRange('M312').getValue();
  const cono_N312 = arquitectura.getRange('N312').getValue();

  const cono_E313 = arquitectura.getRange('E313').getValue();
  const cono_G313 = arquitectura.getRange('G313').getValue();
  const cono_M313 = arquitectura.getRange('M313').getValue();
  const cono_N313 = arquitectura.getRange('N313').getValue();

  const cono_E314 = arquitectura.getRange('E314').getValue();
  const cono_G314 = arquitectura.getRange('G314').getValue();
  const cono_M314 = arquitectura.getRange('M314').getValue();
  const cono_N314 = arquitectura.getRange('N314').getValue();

  const cono_E315 = arquitectura.getRange('E315').getValue();
  const cono_G315 = arquitectura.getRange('G315').getValue();
  const cono_M315 = arquitectura.getRange('M315').getValue();
  const cono_N315 = arquitectura.getRange('N315').getValue();

  const cono_E316 = arquitectura.getRange('E316').getValue();
  const cono_G316 = arquitectura.getRange('G316').getValue();
  const cono_M316 = arquitectura.getRange('M316').getValue();
  const cono_N316 = arquitectura.getRange('N316').getValue();

  const cono_E317 = arquitectura.getRange('E317').getValue();
  const cono_G317 = arquitectura.getRange('G317').getValue();
  const cono_M317 = arquitectura.getRange('M317').getValue();
  const cono_N317 = arquitectura.getRange('N317').getValue();

  const cono_E318 = arquitectura.getRange('E318').getValue();
  const cono_G318 = arquitectura.getRange('G318').getValue();
  const cono_M318 = arquitectura.getRange('M318').getValue();
  const cono_N318 = arquitectura.getRange('N318').getValue();

  const cono_E319 = arquitectura.getRange('E319').getValue();
  const cono_G319 = arquitectura.getRange('G319').getValue();
  const cono_M319 = arquitectura.getRange('M319').getValue();
  const cono_N319 = arquitectura.getRange('N319').getValue();

  const cono_E320 = arquitectura.getRange('E320').getValue();
  const cono_G320 = arquitectura.getRange('G320').getValue();
  const cono_M320 = arquitectura.getRange('M320').getValue();
  const cono_N320 = arquitectura.getRange('N320').getValue();

  const cono_E321 = arquitectura.getRange('E321').getValue();
  const cono_G321 = arquitectura.getRange('G321').getValue();
  const cono_M321 = arquitectura.getRange('M321').getValue();
  const cono_N321 = arquitectura.getRange('N321').getValue();

  const evid_E322 = arquitectura.getRange('E322').getValue();
  const evid_G322 = arquitectura.getRange('G322').getValue();
  const evid_M322 = arquitectura.getRange('M322').getValue();
  const evid_N322 = arquitectura.getRange('N322').getValue();

  const evid_E323 = arquitectura.getRange('E323').getValue();
  const evid_G323 = arquitectura.getRange('G323').getValue();
  const evid_M323 = arquitectura.getRange('M323').getValue();
  const evid_N323 = arquitectura.getRange('N323').getValue();

  const evid_E324 = arquitectura.getRange('E324').getValue();
  const evid_G324 = arquitectura.getRange('G324').getValue();
  const evid_M324 = arquitectura.getRange('M324').getValue();
  const evid_N324 = arquitectura.getRange('N324').getValue();

  const evid_E325 = arquitectura.getRange('E325').getValue();
  const evid_G325 = arquitectura.getRange('G325').getValue();
  const evid_M325 = arquitectura.getRange('M325').getValue();
  const evid_N325 = arquitectura.getRange('N325').getValue();

  const evid_E326 = arquitectura.getRange('E326').getValue();
  const evid_G326 = arquitectura.getRange('G326').getValue();
  const evid_M326 = arquitectura.getRange('M326').getValue();
  const evid_N326 = arquitectura.getRange('N326').getValue();

  const sum_E327 = arquitectura.getRange('E327').getValue();
  const sum_G327 = arquitectura.getRange('G327').getValue();
  const sum_M327 = arquitectura.getRange('M327').getValue();
  const sum_N327 = arquitectura.getRange('N327').getValue();

  const tablaRango327 = arquitectura.getRange(7,4, 327, 11).getValues();

  const lineaTotal327 = arquitectura.getRange(327, 4,1,11).getValues();
  const totalSum327 = lineaTotal327[0][1];

  // Conocimiento No 1
  htmlTemplate.cono_E312 = cono_E312;
  htmlTemplate.cono_G312 = cono_G312;
  htmlTemplate.cono_M312 = cono_M312;
  htmlTemplate.cono_N312 = cono_N312;

  // Conocimiento No 2
  htmlTemplate.cono_E313 = cono_E313;
  htmlTemplate.cono_G313 = cono_G313;
  htmlTemplate.cono_M313 = cono_M313;
  htmlTemplate.cono_N313 = cono_N313;

    // Conocimiento No 3
  htmlTemplate.cono_E314 = cono_E314;
  htmlTemplate.cono_G314 = cono_G314;
  htmlTemplate.cono_M314 = cono_M314;
  htmlTemplate.cono_N314 = cono_N314;

      // Conocimiento No 4
  htmlTemplate.cono_E315 = cono_E315;
  htmlTemplate.cono_G315 = cono_G315;
  htmlTemplate.cono_M315 = cono_M315;
  htmlTemplate.cono_N315 = cono_N315;

  // Conocimiento No 5
  htmlTemplate.cono_E316 = cono_E316;
  htmlTemplate.cono_G316 = cono_G316;
  htmlTemplate.cono_M316 = cono_M316;
  htmlTemplate.cono_N316 = cono_N316;

  // Conocimiento No 6
  htmlTemplate.cono_E317 = cono_E317;
  htmlTemplate.cono_G317 = cono_G317;
  htmlTemplate.cono_M317 = cono_M317;
  htmlTemplate.cono_N317 = cono_N317;

  // Conocimiento No 7
  htmlTemplate.cono_E318 = cono_E318;
  htmlTemplate.cono_G318 = cono_G318;
  htmlTemplate.cono_M318 = cono_M318;
  htmlTemplate.cono_N318 = cono_N318;

    // Conocimiento No 7
  htmlTemplate.cono_E319 = cono_E319;
  htmlTemplate.cono_G319 = cono_G319;
  htmlTemplate.cono_M319 = cono_M319;
  htmlTemplate.cono_N319 = cono_N319;

    // Conocimiento No 8
  htmlTemplate.cono_E320 = cono_E320;
  htmlTemplate.cono_G320 = cono_G320;
  htmlTemplate.cono_M320 = cono_M320;
  htmlTemplate.cono_N320 = cono_N320;

  htmlTemplate.cono_E321 = cono_E321;
  htmlTemplate.cono_G321 = cono_G321;
  htmlTemplate.cono_M321 = cono_M321;
  htmlTemplate.cono_N321 = cono_N321;


        // Evidencia Rotulo
  
// Evidencia No 1
  htmlTemplate.evid_E322 = evid_E322;
  htmlTemplate.evid_G322 = evid_G322;
  htmlTemplate.evid_M322 = evid_M322;
  htmlTemplate.evid_N322 = evid_N322;

  // Evidencia No 2
  htmlTemplate.evid_E323 = evid_E323;
  htmlTemplate.evid_G323 = evid_G323;
  htmlTemplate.evid_M323 = evid_M323;
  htmlTemplate.evid_N323 = evid_N323;

    // Evidencia No 3
  htmlTemplate.evid_E324 = evid_E324;
  htmlTemplate.evid_G324 = evid_G324;
  htmlTemplate.evid_M324 = evid_M324;
  htmlTemplate.evid_N324 = evid_N324;

      // Evidencia No 4
  htmlTemplate.evid_E325 = evid_E325;
  htmlTemplate.evid_G325 = evid_G325;
  htmlTemplate.evid_M325 = evid_M325;
  htmlTemplate.evid_N325 = evid_N325;

        // Evidencia No 4
  htmlTemplate.evid_E326 = evid_E326;
  htmlTemplate.evid_G326 = evid_G326;
  htmlTemplate.evid_M326 = evid_M326;
  htmlTemplate.evid_N326 = evid_N326;

// Suma
  htmlTemplate.sum_E327 = sum_E327;
  htmlTemplate.sum_G327 = sum_G327;
  htmlTemplate.sum_M327 = sum_M327;
  htmlTemplate.sum_N327 = sum_N327;

  htmlTemplate.totalSum327 = totalSum327;
  htmlTemplate.tablaRango327 = tablaRango327

  // =========================================================================================================


  // =========================================================================================================
  // MATEMATICAS

    // Competencia

  const comp_codigo_E339 = arquitectura.getRange('E339').getValue();
  const comp_descrip_F339 = arquitectura.getRange('F339').getValue();

  htmlTemplate.comp_codigo_E339 = comp_codigo_E339;
  htmlTemplate.comp_descrip_F339 = comp_descrip_F339;

  // RAPS

  const rap_E340 = arquitectura.getRange('E340').getValue();
  const rap_F340 = arquitectura.getRange('F340').getValue();
  const rap_M340 = arquitectura.getRange('M340').getValue();
  const rap_N340 = arquitectura.getRange('N340').getValue();

  htmlTemplate.rap_E340 = rap_E340;
  htmlTemplate.rap_F340 = rap_F340;
  htmlTemplate.rap_M340 = rap_M340;
  htmlTemplate.rap_N340 = rap_N340;

  const rap_E341 = arquitectura.getRange('E341').getValue();
  const rap_F341 = arquitectura.getRange('F341').getValue();
  const rap_M341 = arquitectura.getRange('M341').getValue();
  const rap_N341 = arquitectura.getRange('N341').getValue();

  htmlTemplate.rap_E341 = rap_E341;
  htmlTemplate.rap_F341 = rap_F341;
  htmlTemplate.rap_M341 = rap_M341;
  htmlTemplate.rap_N341 = rap_N341;

  const rap_E342 = arquitectura.getRange('E342').getValue();
  const rap_F342 = arquitectura.getRange('F342').getValue();
  const rap_M342 = arquitectura.getRange('M342').getValue();
  const rap_N342 = arquitectura.getRange('N342').getValue();

  htmlTemplate.rap_E342 = rap_E342;
  htmlTemplate.rap_F342 = rap_F342;
  htmlTemplate.rap_M342 = rap_M342;
  htmlTemplate.rap_N342 = rap_N342;

  const rap_E343 = arquitectura.getRange('E343').getValue();
  const rap_F343 = arquitectura.getRange('F343').getValue();
  const rap_M343 = arquitectura.getRange('M343').getValue();
  const rap_N343 = arquitectura.getRange('N343').getValue();

  htmlTemplate.rap_E343 = rap_E343;
  htmlTemplate.rap_F343 = rap_F343;
  htmlTemplate.rap_M343 = rap_M343;
  htmlTemplate.rap_N343 = rap_N343;

  const rap_E344 = arquitectura.getRange('E344').getValue();
  const rap_F344 = arquitectura.getRange('F344').getValue();
  const rap_M344 = arquitectura.getRange('M344').getValue();
  const rap_N344 = arquitectura.getRange('N344').getValue();

  htmlTemplate.rap_E344 = rap_E344;
  htmlTemplate.rap_F344 = rap_F344;
  htmlTemplate.rap_M344 = rap_M344;
  htmlTemplate.rap_N344 = rap_N344;

  const rap_E345 = arquitectura.getRange('E345').getValue();
  const rap_F345 = arquitectura.getRange('F345').getValue();
  const rap_M345 = arquitectura.getRange('M345').getValue();
  const rap_N345 = arquitectura.getRange('N345').getValue();

  htmlTemplate.rap_E345 = rap_E345;
  htmlTemplate.rap_F345 = rap_F345;
  htmlTemplate.rap_M345 = rap_M345;
  htmlTemplate.rap_N345 = rap_N345;

  const rap_E346 = arquitectura.getRange('E346').getValue();
  const rap_F346 = arquitectura.getRange('F346').getValue();
  const rap_M346 = arquitectura.getRange('M346').getValue();
  const rap_N346 = arquitectura.getRange('N346').getValue();

  htmlTemplate.rap_E346 = rap_E346;
  htmlTemplate.rap_F346 = rap_F346;
  htmlTemplate.rap_M346 = rap_M346;
  htmlTemplate.rap_N346 = rap_N346;

  const rap_E347 = arquitectura.getRange('E347').getValue();
  const rap_F347 = arquitectura.getRange('F347').getValue();
  const rap_M347 = arquitectura.getRange('M347').getValue();
  const rap_N347 = arquitectura.getRange('N347').getValue();

  htmlTemplate.rap_E347 = rap_E347;
  htmlTemplate.rap_F347 = rap_F347;
  htmlTemplate.rap_M347 = rap_M347;
  htmlTemplate.rap_N347 = rap_N347;

  // Clasificacion

  const clas_E348 = arquitectura.getRange('E348').getValue();
  const clas_F348 = arquitectura.getRange('F348').getValue();

  htmlTemplate.clas_E348 = clas_E348;
  htmlTemplate.clas_F348 = clas_F348;

  // Conocimientos

  const cono_E349 = arquitectura.getRange('E349').getValue();
  const cono_G349 = arquitectura.getRange('G349').getValue();
  const cono_M349 = arquitectura.getRange('M349').getValue();
  const cono_N349 = arquitectura.getRange('N349').getValue();

  htmlTemplate.cono_E349 = cono_E349;
  htmlTemplate.cono_G349 = cono_G349;
  htmlTemplate.cono_M349 = cono_M349;
  htmlTemplate.cono_N349 = cono_N349;

  const cono_E350 = arquitectura.getRange('E350').getValue();
  const cono_G350 = arquitectura.getRange('G350').getValue();
  const cono_M350 = arquitectura.getRange('M350').getValue();
  const cono_N350 = arquitectura.getRange('N350').getValue();

  htmlTemplate.cono_E350 = cono_E350;
  htmlTemplate.cono_G350 = cono_G350;
  htmlTemplate.cono_M350 = cono_M350;
  htmlTemplate.cono_N350 = cono_N350;

  const cono_E351 = arquitectura.getRange('E351').getValue();
  const cono_G351 = arquitectura.getRange('G351').getValue();
  const cono_M351 = arquitectura.getRange('M351').getValue();
  const cono_N351 = arquitectura.getRange('N351').getValue();

  htmlTemplate.cono_E351 = cono_E351;
  htmlTemplate.cono_G351 = cono_G351;
  htmlTemplate.cono_M351 = cono_M351;
  htmlTemplate.cono_N351 = cono_N351;

  const cono_E352 = arquitectura.getRange('E352').getValue();
  const cono_G352 = arquitectura.getRange('G352').getValue();
  const cono_M352 = arquitectura.getRange('M352').getValue();
  const cono_N352 = arquitectura.getRange('N352').getValue();

  htmlTemplate.cono_E352 = cono_E352;
  htmlTemplate.cono_G352 = cono_G352;
  htmlTemplate.cono_M352 = cono_M352;
  htmlTemplate.cono_N352 = cono_N352;

  const cono_E353 = arquitectura.getRange('E353').getValue();
  const cono_G353 = arquitectura.getRange('G353').getValue();
  const cono_M353 = arquitectura.getRange('M353').getValue();
  const cono_N353 = arquitectura.getRange('N353').getValue();

  htmlTemplate.cono_E353 = cono_E353;
  htmlTemplate.cono_G353 = cono_G353;
  htmlTemplate.cono_M353 = cono_M353;
  htmlTemplate.cono_N353 = cono_N353;

  const cono_E354 = arquitectura.getRange('E354').getValue();
  const cono_G354 = arquitectura.getRange('G354').getValue();
  const cono_M354 = arquitectura.getRange('M354').getValue();
  const cono_N354 = arquitectura.getRange('N354').getValue();

  htmlTemplate.cono_E354 = cono_E354;
  htmlTemplate.cono_G354 = cono_G354;
  htmlTemplate.cono_M354 = cono_M354;
  htmlTemplate.cono_N354 = cono_N354;

  const cono_E355 = arquitectura.getRange('E355').getValue();
  const cono_G355 = arquitectura.getRange('G355').getValue();
  const cono_M355 = arquitectura.getRange('M355').getValue();
  const cono_N355 = arquitectura.getRange('N355').getValue();

  htmlTemplate.cono_E355 = cono_E355;
  htmlTemplate.cono_G355 = cono_G355;
  htmlTemplate.cono_M355 = cono_M355;
  htmlTemplate.cono_N355 = cono_N355;

  const cono_E356 = arquitectura.getRange('E356').getValue();
  const cono_G356 = arquitectura.getRange('G356').getValue();
  const cono_M356 = arquitectura.getRange('M356').getValue();
  const cono_N356 = arquitectura.getRange('N356').getValue();

  htmlTemplate.cono_E356 = cono_E356;
  htmlTemplate.cono_G356 = cono_G356;
  htmlTemplate.cono_M356 = cono_M356;
  htmlTemplate.cono_N356 = cono_N356;

  const cono_E357 = arquitectura.getRange('E357').getValue();
  const cono_G357 = arquitectura.getRange('G357').getValue();
  const cono_M357 = arquitectura.getRange('M357').getValue();
  const cono_N357 = arquitectura.getRange('N357').getValue();

  htmlTemplate.cono_E357 = cono_E357;
  htmlTemplate.cono_G357 = cono_G357;
  htmlTemplate.cono_M357 = cono_M357;
  htmlTemplate.cono_N357 = cono_N357;

  const cono_E358 = arquitectura.getRange('E358').getValue();
  const cono_G358 = arquitectura.getRange('G358').getValue();
  const cono_M358 = arquitectura.getRange('M358').getValue();
  const cono_N358 = arquitectura.getRange('N358').getValue();

  htmlTemplate.cono_E358 = cono_E358;
  htmlTemplate.cono_G358 = cono_G358;
  htmlTemplate.cono_M358 = cono_M358;
  htmlTemplate.cono_N358 = cono_N358;

  // Evidencias

  const evid_E359 = arquitectura.getRange('E359').getValue();
  const evid_G359 = arquitectura.getRange('G359').getValue();
  const evid_M359 = arquitectura.getRange('M359').getValue();
  const evid_N359 = arquitectura.getRange('N359').getValue();

  htmlTemplate.evid_E359 = evid_E359;
  htmlTemplate.evid_G359 = evid_G359;
  htmlTemplate.evid_M359 = evid_M359;
  htmlTemplate.evid_N359 = evid_N359;

  const evid_E360 = arquitectura.getRange('E360').getValue();
  const evid_G360 = arquitectura.getRange('G360').getValue();
  const evid_M360 = arquitectura.getRange('M360').getValue();
  const evid_N360 = arquitectura.getRange('N360').getValue();

  htmlTemplate.evid_E360 = evid_E360;
  htmlTemplate.evid_G360 = evid_G360;
  htmlTemplate.evid_M360 = evid_M360;
  htmlTemplate.evid_N360 = evid_N360;

  const evid_E361 = arquitectura.getRange('E361').getValue();
  const evid_G361 = arquitectura.getRange('G361').getValue();
  const evid_M361 = arquitectura.getRange('M361').getValue();
  const evid_N361 = arquitectura.getRange('N361').getValue();

  htmlTemplate.evid_E361 = evid_E361;
  htmlTemplate.evid_G361 = evid_G361;
  htmlTemplate.evid_M361 = evid_M361;
  htmlTemplate.evid_N361 = evid_N361;

  const evid_E362 = arquitectura.getRange('E362').getValue();
  const evid_G362 = arquitectura.getRange('G362').getValue();
  const evid_M362 = arquitectura.getRange('M362').getValue();
  const evid_N362 = arquitectura.getRange('N362').getValue();

  htmlTemplate.evid_E362 = evid_E362;
  htmlTemplate.evid_G362 = evid_G362;
  htmlTemplate.evid_M362 = evid_M362;
  htmlTemplate.evid_N362 = evid_N362;

  const evid_E363 = arquitectura.getRange('E363').getValue();
  const evid_G363 = arquitectura.getRange('G363').getValue();
  const evid_M363 = arquitectura.getRange('M363').getValue();
  const evid_N363 = arquitectura.getRange('N363').getValue();

  htmlTemplate.evid_E363 = evid_E363;
  htmlTemplate.evid_G363 = evid_G363;
  htmlTemplate.evid_M363 = evid_M363;
  htmlTemplate.evid_N363 = evid_N363;

  const sum_E364 = arquitectura.getRange('E364').getValue();
  const sum_G364 = arquitectura.getRange('G364').getValue();
  const sum_M364 = arquitectura.getRange('M364').getValue();
  const sum_N364 = arquitectura.getRange('N364').getValue();

  htmlTemplate.sum_E364 = sum_E364;
  htmlTemplate.sum_G364 = sum_G364;
  htmlTemplate.sum_M364 = sum_M364;
  htmlTemplate.sum_N364 = sum_N364;

  // Subtotales

  const tablaRango364 = arquitectura.getRange(7,4, 364, 11).getValues();

  const lineaTotal364 = arquitectura.getRange(364, 4,1,11).getValues();
  const totalSum364 = lineaTotal364[0][1];

  htmlTemplate.totalSum364 = totalSum364;
  htmlTemplate.tablaRango364 = tablaRango364

  // =========================================================================================================

  // BIOLOGIA
  const comp_codigo_E374 = arquitectura.getRange('E374').getValue();
  const comp_descrip_F374 = arquitectura.getRange('F374').getValue();

  // Competencia
  htmlTemplate.comp_codigo_E374 = comp_codigo_E374;
  htmlTemplate.comp_descrip_F374 = comp_descrip_F374;

  // RAPS

  const rap_E375 = arquitectura.getRange('E375').getValue();
  const rap_F375 = arquitectura.getRange('F375').getValue();
  const rap_M375 = arquitectura.getRange('M375').getValue();
  const rap_N375 = arquitectura.getRange('N375').getValue();

  htmlTemplate.rap_E375 = rap_E375;
  htmlTemplate.rap_F375 = rap_F375;
  htmlTemplate.rap_M375 = rap_M375;
  htmlTemplate.rap_N375 = rap_N375;

  const rap_E376 = arquitectura.getRange('E376').getValue();
  const rap_F376 = arquitectura.getRange('F376').getValue();
  const rap_M376 = arquitectura.getRange('M376').getValue();
  const rap_N376 = arquitectura.getRange('N376').getValue();

  htmlTemplate.rap_E376 = rap_E376;
  htmlTemplate.rap_F376 = rap_F376;
  htmlTemplate.rap_M376 = rap_M376;
  htmlTemplate.rap_N376 = rap_N376;

  const rap_E377 = arquitectura.getRange('E377').getValue();
  const rap_F377 = arquitectura.getRange('F377').getValue();
  const rap_M377 = arquitectura.getRange('M377').getValue();
  const rap_N377 = arquitectura.getRange('N377').getValue();

  htmlTemplate.rap_E377 = rap_E377;
  htmlTemplate.rap_F377 = rap_F377;
  htmlTemplate.rap_M377 = rap_M377;
  htmlTemplate.rap_N377 = rap_N377;

  const rap_E378 = arquitectura.getRange('E378').getValue();
  const rap_F378 = arquitectura.getRange('F378').getValue();
  const rap_M378 = arquitectura.getRange('M378').getValue();
  const rap_N378 = arquitectura.getRange('N378').getValue();

  htmlTemplate.rap_E378 = rap_E378;
  htmlTemplate.rap_F378 = rap_F378;
  htmlTemplate.rap_M378 = rap_M378;
  htmlTemplate.rap_N378 = rap_N378;

  const rap_E379 = arquitectura.getRange('E379').getValue();
  const rap_F379 = arquitectura.getRange('F379').getValue();
  const rap_M379 = arquitectura.getRange('M379').getValue();
  const rap_N379 = arquitectura.getRange('N379').getValue();

  htmlTemplate.rap_E379 = rap_E379;
  htmlTemplate.rap_F379 = rap_F379;
  htmlTemplate.rap_M379 = rap_M379;
  htmlTemplate.rap_N379 = rap_N379;

  const rap_E380 = arquitectura.getRange('E380').getValue();
  const rap_F380 = arquitectura.getRange('F380').getValue();
  const rap_M380 = arquitectura.getRange('M380').getValue();
  const rap_N380 = arquitectura.getRange('N380').getValue();

  htmlTemplate.rap_E380 = rap_E380;
  htmlTemplate.rap_F380 = rap_F380;
  htmlTemplate.rap_M380 = rap_M380;
  htmlTemplate.rap_N380 = rap_N380;

  const rap_E381 = arquitectura.getRange('E381').getValue();
  const rap_F381 = arquitectura.getRange('F381').getValue();
  const rap_M381 = arquitectura.getRange('M381').getValue();
  const rap_N381 = arquitectura.getRange('N381').getValue();

  htmlTemplate.rap_E381 = rap_E381;
  htmlTemplate.rap_F381 = rap_F381;
  htmlTemplate.rap_M381 = rap_M381;
  htmlTemplate.rap_N381 = rap_N381;

  const rap_E382 = arquitectura.getRange('E382').getValue();
  const rap_F382 = arquitectura.getRange('F382').getValue();
  const rap_M382 = arquitectura.getRange('M382').getValue();
  const rap_N382 = arquitectura.getRange('N382').getValue();

  htmlTemplate.rap_E382 = rap_E382;
  htmlTemplate.rap_F382 = rap_F382;
  htmlTemplate.rap_M382 = rap_M382;
  htmlTemplate.rap_N382 = rap_N382;

  // Clasificacion

  const clas_E383 = arquitectura.getRange('E383').getValue();
  const clas_F383 = arquitectura.getRange('F383').getValue();

  htmlTemplate.clas_E383 = clas_E383;
  htmlTemplate.clas_F383 = clas_F383;

  // Conocimientos

  const cono_E384 = arquitectura.getRange('E384').getValue();
  const cono_G384 = arquitectura.getRange('G384').getValue();
  const cono_M384 = arquitectura.getRange('M384').getValue();
  const cono_N384 = arquitectura.getRange('N384').getValue();

  htmlTemplate.cono_E384 = cono_E384;
  htmlTemplate.cono_G384 = cono_G384;
  htmlTemplate.cono_M384 = cono_M384;
  htmlTemplate.cono_N384 = cono_N384;

  const cono_E385 = arquitectura.getRange('E385').getValue();
  const cono_G385 = arquitectura.getRange('G385').getValue();
  const cono_M385 = arquitectura.getRange('M385').getValue();
  const cono_N385 = arquitectura.getRange('N385').getValue();

  htmlTemplate.cono_E385 = cono_E385;
  htmlTemplate.cono_G385 = cono_G385;
  htmlTemplate.cono_M385 = cono_M385;
  htmlTemplate.cono_N385 = cono_N385;

  const cono_E386 = arquitectura.getRange('E386').getValue();
  const cono_G386 = arquitectura.getRange('G386').getValue();
  const cono_M386 = arquitectura.getRange('M386').getValue();
  const cono_N386 = arquitectura.getRange('N386').getValue();

  htmlTemplate.cono_E386 = cono_E386;
  htmlTemplate.cono_G386 = cono_G386;
  htmlTemplate.cono_M386 = cono_M386;
  htmlTemplate.cono_N386 = cono_N386;

  const cono_E387 = arquitectura.getRange('E387').getValue();
  const cono_G387 = arquitectura.getRange('G387').getValue();
  const cono_M387 = arquitectura.getRange('M387').getValue();
  const cono_N387 = arquitectura.getRange('N387').getValue();

  htmlTemplate.cono_E387 = cono_E387;
  htmlTemplate.cono_G387 = cono_G387;
  htmlTemplate.cono_M387 = cono_M387;
  htmlTemplate.cono_N387 = cono_N387;

  const cono_E388 = arquitectura.getRange('E388').getValue();
  const cono_G388 = arquitectura.getRange('G388').getValue();
  const cono_M388 = arquitectura.getRange('M388').getValue();
  const cono_N388 = arquitectura.getRange('N388').getValue();

  htmlTemplate.cono_E388 = cono_E388;
  htmlTemplate.cono_G388 = cono_G388;
  htmlTemplate.cono_M388 = cono_M388;
  htmlTemplate.cono_N388 = cono_N388;

  const cono_E389 = arquitectura.getRange('E389').getValue();
  const cono_G389 = arquitectura.getRange('G389').getValue();
  const cono_M389 = arquitectura.getRange('M389').getValue();
  const cono_N389 = arquitectura.getRange('N389').getValue();

  htmlTemplate.cono_E389 = cono_E389;
  htmlTemplate.cono_G389 = cono_G389;
  htmlTemplate.cono_M389 = cono_M389;
  htmlTemplate.cono_N389 = cono_N389;

  const cono_E390 = arquitectura.getRange('E390').getValue();
  const cono_G390 = arquitectura.getRange('G390').getValue();
  const cono_M390 = arquitectura.getRange('M390').getValue();
  const cono_N390 = arquitectura.getRange('N390').getValue();

  htmlTemplate.cono_E390 = cono_E390;
  htmlTemplate.cono_G390 = cono_G390;
  htmlTemplate.cono_M390 = cono_M390;
  htmlTemplate.cono_N390 = cono_N390;

  const cono_E391 = arquitectura.getRange('E391').getValue();
  const cono_G391 = arquitectura.getRange('G391').getValue();
  const cono_M391 = arquitectura.getRange('M391').getValue();
  const cono_N391 = arquitectura.getRange('N391').getValue();

  htmlTemplate.cono_E391 = cono_E391;
  htmlTemplate.cono_G391 = cono_G391;
  htmlTemplate.cono_M391 = cono_M391;
  htmlTemplate.cono_N391 = cono_N391;

  const cono_E392 = arquitectura.getRange('E392').getValue();
  const cono_G392 = arquitectura.getRange('G392').getValue();
  const cono_M392 = arquitectura.getRange('M392').getValue();
  const cono_N392 = arquitectura.getRange('N392').getValue();

  htmlTemplate.cono_E392 = cono_E392;
  htmlTemplate.cono_G392 = cono_G392;
  htmlTemplate.cono_M392 = cono_M392;
  htmlTemplate.cono_N392 = cono_N392;

  const cono_E393 = arquitectura.getRange('E393').getValue();
  const cono_G393 = arquitectura.getRange('G393').getValue();
  const cono_M393 = arquitectura.getRange('M393').getValue();
  const cono_N393 = arquitectura.getRange('N393').getValue();

  htmlTemplate.cono_E393 = cono_E393;
  htmlTemplate.cono_G393 = cono_G393;
  htmlTemplate.cono_M393 = cono_M393;
  htmlTemplate.cono_N393 = cono_N393;

  // Evidencias

  const evid_E394 = arquitectura.getRange('E394').getValue();
  const evid_G394 = arquitectura.getRange('G394').getValue();
  const evid_M394 = arquitectura.getRange('M394').getValue();
  const evid_N394 = arquitectura.getRange('N394').getValue();

  htmlTemplate.evid_E394 = evid_E394;
  htmlTemplate.evid_G394 = evid_G394;
  htmlTemplate.evid_M394 = evid_M394;
  htmlTemplate.evid_N394 = evid_N394;

  const evid_E395 = arquitectura.getRange('E395').getValue();
  const evid_G395 = arquitectura.getRange('G395').getValue();
  const evid_M395 = arquitectura.getRange('M395').getValue();
  const evid_N395 = arquitectura.getRange('N395').getValue();

  htmlTemplate.evid_E395 = evid_E395;
  htmlTemplate.evid_G395 = evid_G395;
  htmlTemplate.evid_M395 = evid_M395;
  htmlTemplate.evid_N395 = evid_N395;

  const evid_E396 = arquitectura.getRange('E396').getValue();
  const evid_G396 = arquitectura.getRange('G396').getValue();
  const evid_M396 = arquitectura.getRange('M396').getValue();
  const evid_N396 = arquitectura.getRange('N396').getValue();

  htmlTemplate.evid_E396 = evid_E396;
  htmlTemplate.evid_G396 = evid_G396;
  htmlTemplate.evid_M396 = evid_M396;
  htmlTemplate.evid_N396 = evid_N396;

  const evid_E397 = arquitectura.getRange('E397').getValue();
  const evid_G397 = arquitectura.getRange('G397').getValue();
  const evid_M397 = arquitectura.getRange('M397').getValue();
  const evid_N397 = arquitectura.getRange('N397').getValue();

  htmlTemplate.evid_E397 = evid_E397;
  htmlTemplate.evid_G397 = evid_G397;
  htmlTemplate.evid_M397 = evid_M397;
  htmlTemplate.evid_N397 = evid_N397;

  const evid_E398 = arquitectura.getRange('E398').getValue();
  const evid_G398 = arquitectura.getRange('G398').getValue();
  const evid_M398 = arquitectura.getRange('M398').getValue();
  const evid_N398 = arquitectura.getRange('N398').getValue();

  htmlTemplate.evid_E398 = evid_E398;
  htmlTemplate.evid_G398 = evid_G398;
  htmlTemplate.evid_M398 = evid_M398;
  htmlTemplate.evid_N398 = evid_N398;

  const sum_E399 = arquitectura.getRange('E399').getValue();
  const sum_G399 = arquitectura.getRange('G399').getValue();
  const sum_M399 = arquitectura.getRange('M399').getValue();
  const sum_N399 = arquitectura.getRange('N399').getValue();

  htmlTemplate.sum_E399 = sum_E399;
  htmlTemplate.sum_G399 = sum_G399;
  htmlTemplate.sum_M399 = sum_M399;
  htmlTemplate.sum_N399 = sum_N399;

  // Subtotales

  const tablaRango399 = arquitectura.getRange(7,4, 399, 11).getValues();

  const lineaTotal399 = arquitectura.getRange(399, 4,1,11).getValues();
  const totalSum399 = lineaTotal399[0][1];

  htmlTemplate.totalSum399 = totalSum399;
  htmlTemplate.tablaRango399 = tablaRango399

   // =========================================================================================================

  // COMUNICACIÓN ORAL Y ESCRITA
  const comp_codigo_E409 = arquitectura.getRange('E409').getValue();
  const comp_descrip_F409 = arquitectura.getRange('F409').getValue();

  // Competencia
  htmlTemplate.comp_codigo_E409 = comp_codigo_E409;
  htmlTemplate.comp_descrip_F409 = comp_descrip_F409;

  // RAPS

  const rap_E410 = arquitectura.getRange('E410').getValue();
  const rap_F410 = arquitectura.getRange('F410').getValue();
  const rap_M410 = arquitectura.getRange('M410').getValue();
  const rap_N410 = arquitectura.getRange('N410').getValue();

  htmlTemplate.rap_E410 = rap_E410;
  htmlTemplate.rap_F410 = rap_F410;
  htmlTemplate.rap_M410 = rap_M410;
  htmlTemplate.rap_N410 = rap_N410;

  const rap_E411 = arquitectura.getRange('E411').getValue();
  const rap_F411 = arquitectura.getRange('F411').getValue();
  const rap_M411 = arquitectura.getRange('M411').getValue();
  const rap_N411 = arquitectura.getRange('N411').getValue();

  htmlTemplate.rap_E411 = rap_E411;
  htmlTemplate.rap_F411 = rap_F411;
  htmlTemplate.rap_M411 = rap_M411;
  htmlTemplate.rap_N411 = rap_N411;

  const rap_E412 = arquitectura.getRange('E412').getValue();
  const rap_F412 = arquitectura.getRange('F412').getValue();
  const rap_M412 = arquitectura.getRange('M412').getValue();
  const rap_N412 = arquitectura.getRange('N412').getValue();

  htmlTemplate.rap_E412 = rap_E412;
  htmlTemplate.rap_F412 = rap_F412;
  htmlTemplate.rap_M412 = rap_M412;
  htmlTemplate.rap_N412 = rap_N412;

  const rap_E413 = arquitectura.getRange('E413').getValue();
  const rap_F413 = arquitectura.getRange('F413').getValue();
  const rap_M413 = arquitectura.getRange('M413').getValue();
  const rap_N413 = arquitectura.getRange('N413').getValue();

  htmlTemplate.rap_E413 = rap_E413;
  htmlTemplate.rap_F413 = rap_F413;
  htmlTemplate.rap_M413 = rap_M413;
  htmlTemplate.rap_N413 = rap_N413;

  const rap_E414 = arquitectura.getRange('E414').getValue();
  const rap_F414 = arquitectura.getRange('F414').getValue();
  const rap_M414 = arquitectura.getRange('M414').getValue();
  const rap_N414 = arquitectura.getRange('N414').getValue();

  htmlTemplate.rap_E414 = rap_E414;
  htmlTemplate.rap_F414 = rap_F414;
  htmlTemplate.rap_M414 = rap_M414;
  htmlTemplate.rap_N414 = rap_N414;

  const rap_E415 = arquitectura.getRange('E415').getValue();
  const rap_F415 = arquitectura.getRange('F415').getValue();
  const rap_M415 = arquitectura.getRange('M415').getValue();
  const rap_N415 = arquitectura.getRange('N415').getValue();

  htmlTemplate.rap_E415 = rap_E415;
  htmlTemplate.rap_F415 = rap_F415;
  htmlTemplate.rap_M415 = rap_M415;
  htmlTemplate.rap_N415 = rap_N415;

  const rap_E416 = arquitectura.getRange('E416').getValue();
  const rap_F416 = arquitectura.getRange('G416').getValue();
  const rap_M416 = arquitectura.getRange('M416').getValue();
  const rap_N416 = arquitectura.getRange('N416').getValue();

  htmlTemplate.rap_E416 = rap_E416;
  htmlTemplate.rap_F416 = rap_F416;
  htmlTemplate.rap_M416 = rap_M416;
  htmlTemplate.rap_N416 = rap_N416;

  const rap_E417 = arquitectura.getRange('E417').getValue();
  const rap_F417 = arquitectura.getRange('F417').getValue();
  const rap_M417 = arquitectura.getRange('M417').getValue();
  const rap_N417 = arquitectura.getRange('N417').getValue();

  htmlTemplate.rap_E417 = rap_E417;
  htmlTemplate.rap_F417 = rap_F417;
  htmlTemplate.rap_M417 = rap_M417;
  htmlTemplate.rap_N417 = rap_N417;

  // Clasificacion

  const clas_E418 = arquitectura.getRange('E418').getValue();
  const clas_F418 = arquitectura.getRange('F418').getValue();


  htmlTemplate.clas_E418 = clas_E418;
  htmlTemplate.clas_F418 = clas_F418;

  // Conocimientos

  const cono_E419 = arquitectura.getRange('E419').getValue();
  const cono_G419 = arquitectura.getRange('G419').getValue();
  const cono_M419 = arquitectura.getRange('M419').getValue();
  const cono_N419 = arquitectura.getRange('N419').getValue();

  htmlTemplate.cono_E419 = cono_E419;
  htmlTemplate.cono_G419 = cono_G419;
  htmlTemplate.cono_M419 = cono_M419;
  htmlTemplate.cono_N419 = cono_N419;

  const cono_E420 = arquitectura.getRange('E420').getValue();
  const cono_G420 = arquitectura.getRange('G420').getValue();
  const cono_M420 = arquitectura.getRange('M420').getValue();
  const cono_N420 = arquitectura.getRange('N420').getValue();

  htmlTemplate.cono_E420 = cono_E420;
  htmlTemplate.cono_G420 = cono_G420;
  htmlTemplate.cono_M420 = cono_M420;
  htmlTemplate.cono_N420 = cono_N420;

  const cono_E421 = arquitectura.getRange('E421').getValue();
  const cono_G421 = arquitectura.getRange('G421').getValue();
  const cono_M421 = arquitectura.getRange('M421').getValue();
  const cono_N421 = arquitectura.getRange('N421').getValue();

  htmlTemplate.cono_E421 = cono_E421;
  htmlTemplate.cono_G421 = cono_G421;
  htmlTemplate.cono_M421 = cono_M421;
  htmlTemplate.cono_N421 = cono_N421;

  const cono_E422 = arquitectura.getRange('E422').getValue();
  const cono_G422 = arquitectura.getRange('G422').getValue();
  const cono_M422 = arquitectura.getRange('M422').getValue();
  const cono_N422 = arquitectura.getRange('N422').getValue();

  htmlTemplate.cono_E422 = cono_E422;
  htmlTemplate.cono_G422 = cono_G422;
  htmlTemplate.cono_M422 = cono_M422;
  htmlTemplate.cono_N422 = cono_N422;

  const cono_E423 = arquitectura.getRange('E423').getValue();
  const cono_G423 = arquitectura.getRange('G423').getValue();
  const cono_M423 = arquitectura.getRange('M423').getValue();
  const cono_N423 = arquitectura.getRange('N423').getValue();

  htmlTemplate.cono_E423 = cono_E423;
  htmlTemplate.cono_G423 = cono_G423;
  htmlTemplate.cono_M423 = cono_M423;
  htmlTemplate.cono_N423 = cono_N423;

  const cono_E424 = arquitectura.getRange('E424').getValue();
  const cono_G424 = arquitectura.getRange('G424').getValue();
  const cono_M424 = arquitectura.getRange('M424').getValue();
  const cono_N424 = arquitectura.getRange('N424').getValue();

  htmlTemplate.cono_E424 = cono_E424;
  htmlTemplate.cono_G424 = cono_G424;
  htmlTemplate.cono_M424 = cono_M424;
  htmlTemplate.cono_N424 = cono_N424;

  const cono_E425 = arquitectura.getRange('E425').getValue();
  const cono_G425 = arquitectura.getRange('G425').getValue();
  const cono_M425 = arquitectura.getRange('M425').getValue();
  const cono_N425 = arquitectura.getRange('N425').getValue();

  htmlTemplate.cono_E425 = cono_E425;
  htmlTemplate.cono_G425 = cono_G425;
  htmlTemplate.cono_M425 = cono_M425;
  htmlTemplate.cono_N425 = cono_N425;

  const cono_E426 = arquitectura.getRange('E426').getValue();
  const cono_G426 = arquitectura.getRange('G426').getValue();
  const cono_M426 = arquitectura.getRange('M426').getValue();
  const cono_N426 = arquitectura.getRange('N426').getValue();

  htmlTemplate.cono_E426 = cono_E426;
  htmlTemplate.cono_G426 = cono_G426;
  htmlTemplate.cono_M426 = cono_M426;
  htmlTemplate.cono_N426 = cono_N426;

  const cono_E427 = arquitectura.getRange('E427').getValue();
  const cono_G427 = arquitectura.getRange('G427').getValue();
  const cono_M427 = arquitectura.getRange('M427').getValue();
  const cono_N427 = arquitectura.getRange('N427').getValue();

  htmlTemplate.cono_E427 = cono_E427;
  htmlTemplate.cono_G427 = cono_G427;
  htmlTemplate.cono_M427 = cono_M427;
  htmlTemplate.cono_N427 = cono_N427;

  const cono_E428 = arquitectura.getRange('E428').getValue();
  const cono_G428 = arquitectura.getRange('G428').getValue();
  const cono_M428 = arquitectura.getRange('M428').getValue();
  const cono_N428 = arquitectura.getRange('N428').getValue();

  htmlTemplate.cono_E428 = cono_E428;
  htmlTemplate.cono_G428 = cono_G428;
  htmlTemplate.cono_M428 = cono_M428;
  htmlTemplate.cono_N428 = cono_N428;

  // Evidencias

  const evid_E429 = arquitectura.getRange('E429').getValue();
  const evid_G429 = arquitectura.getRange('G429').getValue();
  const evid_M429 = arquitectura.getRange('M429').getValue();
  const evid_N429 = arquitectura.getRange('N429').getValue();

  htmlTemplate.evid_E429 = evid_E429;
  htmlTemplate.evid_G429 = evid_G429;
  htmlTemplate.evid_M429 = evid_M429;
  htmlTemplate.evid_N429 = evid_N429;

  const evid_E430 = arquitectura.getRange('E430').getValue();
  const evid_G430 = arquitectura.getRange('G430').getValue();
  const evid_M430 = arquitectura.getRange('M430').getValue();
  const evid_N430 = arquitectura.getRange('N430').getValue();

  htmlTemplate.evid_E430 = evid_E430;
  htmlTemplate.evid_G430 = evid_G430;
  htmlTemplate.evid_M430 = evid_M430;
  htmlTemplate.evid_N430 = evid_N430;

  const evid_E431 = arquitectura.getRange('E431').getValue();
  const evid_G431 = arquitectura.getRange('G431').getValue();
  const evid_M431 = arquitectura.getRange('M431').getValue();
  const evid_N431 = arquitectura.getRange('N431').getValue();

  htmlTemplate.evid_E431 = evid_E431;
  htmlTemplate.evid_G431 = evid_G431;
  htmlTemplate.evid_M431 = evid_M431;
  htmlTemplate.evid_N431 = evid_N431;

  const evid_E432 = arquitectura.getRange('E432').getValue();
  const evid_G432 = arquitectura.getRange('G432').getValue();
  const evid_M432 = arquitectura.getRange('M432').getValue();
  const evid_N432 = arquitectura.getRange('N432').getValue();

  htmlTemplate.evid_E432 = evid_E432;
  htmlTemplate.evid_G432 = evid_G432;
  htmlTemplate.evid_M432 = evid_M432;
  htmlTemplate.evid_N432 = evid_N432;

  const evid_E433 = arquitectura.getRange('E433').getValue();
  const evid_G433 = arquitectura.getRange('G433').getValue();
  const evid_M433 = arquitectura.getRange('M433').getValue();
  const evid_N433 = arquitectura.getRange('N433').getValue();

  htmlTemplate.evid_E433 = evid_E433;
  htmlTemplate.evid_G433 = evid_G433;
  htmlTemplate.evid_M433 = evid_M433;
  htmlTemplate.evid_N433 = evid_N433;

  const sum_E434 = arquitectura.getRange('E434').getValue();
  const sum_G434 = arquitectura.getRange('G434').getValue();
  const sum_M434 = arquitectura.getRange('M434').getValue();
  const sum_N434 = arquitectura.getRange('N434').getValue();

  htmlTemplate.sum_E434 = sum_E434;
  htmlTemplate.sum_G434 = sum_G434;
  htmlTemplate.sum_M434 = sum_M434;
  htmlTemplate.sum_N434 = sum_N434;

  // Subtotales

  const tablaRango434 = arquitectura.getRange(7,4, 434, 11).getValues();

  const lineaTotal434 = arquitectura.getRange(434, 4,1,11).getValues();
  const totalSum434 = lineaTotal434[0][1];

  htmlTemplate.totalSum434 = totalSum434;
  htmlTemplate.tablaRango434 = tablaRango434

     // =========================================================================================================

  // INVESTIGACION
  const comp_codigo_E481 = arquitectura.getRange('E481').getValue();
  const comp_descrip_F481 = arquitectura.getRange('F481').getValue();

  // Competencia
  htmlTemplate.comp_codigo_E481 = comp_codigo_E481;
  htmlTemplate.comp_descrip_F481 = comp_descrip_F481;

  // RAPS

  const rap_E482 = arquitectura.getRange('E482').getValue();
  const rap_F482 = arquitectura.getRange('F482').getValue();
  const rap_M482 = arquitectura.getRange('M482').getValue();
  const rap_N482 = arquitectura.getRange('N482').getValue();

  htmlTemplate.rap_E482 = rap_E482;
  htmlTemplate.rap_F482 = rap_F482;
  htmlTemplate.rap_M482 = rap_M482;
  htmlTemplate.rap_N482 = rap_N482;

  const rap_E483 = arquitectura.getRange('E483').getValue();
  const rap_F483 = arquitectura.getRange('F483').getValue();
  const rap_M483 = arquitectura.getRange('M483').getValue();
  const rap_N483 = arquitectura.getRange('N483').getValue();

  htmlTemplate.rap_E483 = rap_E483;
  htmlTemplate.rap_F483 = rap_F483;
  htmlTemplate.rap_M483 = rap_M483;
  htmlTemplate.rap_N483 = rap_N483;

  const rap_E484 = arquitectura.getRange('E484').getValue();
  const rap_F484 = arquitectura.getRange('F484').getValue();
  const rap_M484 = arquitectura.getRange('M484').getValue();
  const rap_N484 = arquitectura.getRange('N484').getValue();

  htmlTemplate.rap_E484 = rap_E484;
  htmlTemplate.rap_F484 = rap_F484;
  htmlTemplate.rap_M484 = rap_M484;
  htmlTemplate.rap_N484 = rap_N484;

  const rap_E485 = arquitectura.getRange('E485').getValue();
  const rap_F485 = arquitectura.getRange('F485').getValue();
  const rap_M485 = arquitectura.getRange('M485').getValue();
  const rap_N485 = arquitectura.getRange('N485').getValue();

  htmlTemplate.rap_E485 = rap_E485;
  htmlTemplate.rap_F485 = rap_F485;
  htmlTemplate.rap_M485 = rap_M485;
  htmlTemplate.rap_N485 = rap_N485;

  const rap_E486 = arquitectura.getRange('E486').getValue();
  const rap_F486 = arquitectura.getRange('F486').getValue();
  const rap_M486 = arquitectura.getRange('M486').getValue();
  const rap_N486 = arquitectura.getRange('N486').getValue();

  htmlTemplate.rap_E486 = rap_E486;
  htmlTemplate.rap_F486 = rap_F486;
  htmlTemplate.rap_M486 = rap_M486;
  htmlTemplate.rap_N486 = rap_N486;

  const rap_E487 = arquitectura.getRange('E487').getValue();
  const rap_F487 = arquitectura.getRange('F487').getValue();
  const rap_M487 = arquitectura.getRange('M487').getValue();
  const rap_N487 = arquitectura.getRange('N487').getValue();

  htmlTemplate.rap_E487 = rap_E487;
  htmlTemplate.rap_F487 = rap_F487;
  htmlTemplate.rap_M487 = rap_M487;
  htmlTemplate.rap_N487 = rap_N487;

  const rap_E488 = arquitectura.getRange('E488').getValue();
  const rap_F488 = arquitectura.getRange('G488').getValue();
  const rap_M488 = arquitectura.getRange('M488').getValue();
  const rap_N488 = arquitectura.getRange('N488').getValue();

  htmlTemplate.rap_E488 = rap_E488;
  htmlTemplate.rap_F488 = rap_F488;
  htmlTemplate.rap_M488 = rap_M488;
  htmlTemplate.rap_N488 = rap_N488;

  const rap_E489 = arquitectura.getRange('E489').getValue();
  const rap_F489 = arquitectura.getRange('F489').getValue();
  const rap_M489 = arquitectura.getRange('M489').getValue();
  const rap_N489 = arquitectura.getRange('N489').getValue();

  htmlTemplate.rap_E489 = rap_E489;
  htmlTemplate.rap_F489 = rap_F489;
  htmlTemplate.rap_M489 = rap_M489;
  htmlTemplate.rap_N489 = rap_N489;

  // Clasificacion

  const clas_E490 = arquitectura.getRange('E490').getValue();
  const clas_F490 = arquitectura.getRange('F490').getValue();

  htmlTemplate.clas_E490 = clas_E490;
  htmlTemplate.clas_F490 = clas_F490;

  // Conocimientos

  const cono_E491 = arquitectura.getRange('E491').getValue();
  const cono_G491 = arquitectura.getRange('G491').getValue();
  const cono_M491 = arquitectura.getRange('M491').getValue();
  const cono_N491 = arquitectura.getRange('N491').getValue();

  htmlTemplate.cono_E491 = cono_E491;
  htmlTemplate.cono_G491 = cono_G491;
  htmlTemplate.cono_M491 = cono_M491;
  htmlTemplate.cono_N491 = cono_N491;

  const cono_E492 = arquitectura.getRange('E492').getValue();
  const cono_G492 = arquitectura.getRange('G492').getValue();
  const cono_M492 = arquitectura.getRange('M492').getValue();
  const cono_N492 = arquitectura.getRange('N492').getValue();

  htmlTemplate.cono_E492 = cono_E492;
  htmlTemplate.cono_G492 = cono_G492;
  htmlTemplate.cono_M492 = cono_M492;
  htmlTemplate.cono_N492 = cono_N492;

  const cono_E493 = arquitectura.getRange('E493').getValue();
  const cono_G493 = arquitectura.getRange('G493').getValue();
  const cono_M493 = arquitectura.getRange('M493').getValue();
  const cono_N493 = arquitectura.getRange('N493').getValue();

  htmlTemplate.cono_E493 = cono_E493;
  htmlTemplate.cono_G493 = cono_G493;
  htmlTemplate.cono_M493 = cono_M493;
  htmlTemplate.cono_N493 = cono_N493;

  const cono_E494 = arquitectura.getRange('E494').getValue();
  const cono_G494 = arquitectura.getRange('G494').getValue();
  const cono_M494 = arquitectura.getRange('M494').getValue();
  const cono_N494 = arquitectura.getRange('N494').getValue();

  htmlTemplate.cono_E494 = cono_E494;
  htmlTemplate.cono_G494 = cono_G494;
  htmlTemplate.cono_M494 = cono_M494;
  htmlTemplate.cono_N494 = cono_N494;

  const cono_E495 = arquitectura.getRange('E495').getValue();
  const cono_G495 = arquitectura.getRange('G495').getValue();
  const cono_M495 = arquitectura.getRange('M495').getValue();
  const cono_N495 = arquitectura.getRange('N495').getValue();

  htmlTemplate.cono_E495 = cono_E495;
  htmlTemplate.cono_G495 = cono_G495;
  htmlTemplate.cono_M495 = cono_M495;
  htmlTemplate.cono_N495 = cono_N495;

  const cono_E496 = arquitectura.getRange('E496').getValue();
  const cono_G496 = arquitectura.getRange('G496').getValue();
  const cono_M496 = arquitectura.getRange('M496').getValue();
  const cono_N496 = arquitectura.getRange('N496').getValue();

  htmlTemplate.cono_E496 = cono_E496;
  htmlTemplate.cono_G496 = cono_G496;
  htmlTemplate.cono_M496 = cono_M496;
  htmlTemplate.cono_N496 = cono_N496;

  const cono_E497 = arquitectura.getRange('E497').getValue();
  const cono_G497 = arquitectura.getRange('G497').getValue();
  const cono_M497 = arquitectura.getRange('M497').getValue();
  const cono_N497 = arquitectura.getRange('N497').getValue();

  htmlTemplate.cono_E497 = cono_E497;
  htmlTemplate.cono_G497 = cono_G497;
  htmlTemplate.cono_M497 = cono_M497;
  htmlTemplate.cono_N497 = cono_N497;

  const cono_E498 = arquitectura.getRange('E498').getValue();
  const cono_G498 = arquitectura.getRange('G498').getValue();
  const cono_M498 = arquitectura.getRange('M498').getValue();
  const cono_N498 = arquitectura.getRange('N498').getValue();

  htmlTemplate.cono_E498 = cono_E498;
  htmlTemplate.cono_G498 = cono_G498;
  htmlTemplate.cono_M498 = cono_M498;
  htmlTemplate.cono_N498 = cono_N498;

  const cono_E499 = arquitectura.getRange('E499').getValue();
  const cono_G499 = arquitectura.getRange('G499').getValue();
  const cono_M499 = arquitectura.getRange('M499').getValue();
  const cono_N499 = arquitectura.getRange('N499').getValue();

  htmlTemplate.cono_E499 = cono_E499;
  htmlTemplate.cono_G499 = cono_G499;
  htmlTemplate.cono_M499 = cono_M499;
  htmlTemplate.cono_N499 = cono_N499;

  const cono_E500 = arquitectura.getRange('E500').getValue();
  const cono_G500 = arquitectura.getRange('G500').getValue();
  const cono_M500 = arquitectura.getRange('M500').getValue();
  const cono_N500 = arquitectura.getRange('N500').getValue();

  htmlTemplate.cono_E500 = cono_E500;
  htmlTemplate.cono_G500 = cono_G500;
  htmlTemplate.cono_M500 = cono_M500;
  htmlTemplate.cono_N500 = cono_N500;

  // Evidencias

  const evid_E501 = arquitectura.getRange('E501').getValue();
  const evid_G501 = arquitectura.getRange('G501').getValue();
  const evid_M501 = arquitectura.getRange('M501').getValue();
  const evid_N501 = arquitectura.getRange('N501').getValue();

  htmlTemplate.evid_E501 = evid_E501;
  htmlTemplate.evid_G501 = evid_G501;
  htmlTemplate.evid_M501 = evid_M501;
  htmlTemplate.evid_N501 = evid_N501;

  const evid_E502 = arquitectura.getRange('E502').getValue();
  const evid_G502 = arquitectura.getRange('G502').getValue();
  const evid_M502 = arquitectura.getRange('M502').getValue();
  const evid_N502 = arquitectura.getRange('N502').getValue();

  htmlTemplate.evid_E502 = evid_E502;
  htmlTemplate.evid_G502 = evid_G502;
  htmlTemplate.evid_M502 = evid_M502;
  htmlTemplate.evid_N502 = evid_N502;

  const evid_E503 = arquitectura.getRange('E503').getValue();
  const evid_G503 = arquitectura.getRange('G503').getValue();
  const evid_M503 = arquitectura.getRange('M503').getValue();
  const evid_N503 = arquitectura.getRange('N503').getValue();

  htmlTemplate.evid_E503 = evid_E503;
  htmlTemplate.evid_G503 = evid_G503;
  htmlTemplate.evid_M503 = evid_M503;
  htmlTemplate.evid_N503 = evid_N503;

  const evid_E504 = arquitectura.getRange('E504').getValue();
  const evid_G504 = arquitectura.getRange('G504').getValue();
  const evid_M504 = arquitectura.getRange('M504').getValue();
  const evid_N504 = arquitectura.getRange('N504').getValue();

  htmlTemplate.evid_E504 = evid_E504;
  htmlTemplate.evid_G504 = evid_G504;
  htmlTemplate.evid_M504 = evid_M504;
  htmlTemplate.evid_N504 = evid_N504;

  const evid_E505 = arquitectura.getRange('E505').getValue();
  const evid_G505 = arquitectura.getRange('G505').getValue();
  const evid_M505 = arquitectura.getRange('M505').getValue();
  const evid_N505 = arquitectura.getRange('N505').getValue();

  htmlTemplate.evid_E505 = evid_E505;
  htmlTemplate.evid_G505 = evid_G505;
  htmlTemplate.evid_M505 = evid_M505;
  htmlTemplate.evid_N505 = evid_N505;

  const sum_E506 = arquitectura.getRange('E506').getValue();
  const sum_G506 = arquitectura.getRange('G506').getValue();
  const sum_M506 = arquitectura.getRange('M506').getValue();
  const sum_N506 = arquitectura.getRange('N506').getValue();

  htmlTemplate.sum_E506 = sum_E506;
  htmlTemplate.sum_G506 = sum_G506;
  htmlTemplate.sum_M506 = sum_M506;
  htmlTemplate.sum_N506 = sum_N506;

  // Subtotales

  const tablaRango506 = arquitectura.getRange(7,4, 506, 11).getValues();

  const lineaTotal506 = arquitectura.getRange(506, 4,1,11).getValues();
  const totalSum506 = lineaTotal506[0][1];

  htmlTemplate.totalSum506 = totalSum506;
  htmlTemplate.tablaRango506 = tablaRango506

   // ========================================================================================================
  // CONFIGURACIÓN DE TIEMPOS
  const hoja_time = SpreadsheetApp.getActiveSpreadsheet();
  const time = hoja_time.getSheetByName('TIME');

  // FASE

  const fase_directo_C22 = time.getRange('C22').getValue();
  const fase_directo_D22 = time.getRange('D22').getValue();
  const fase_autonomo_E22 = time.getRange('E22').getValue();
  const fase_autonomo_F22 = time.getRange('F22').getValue();

  htmlTemplate.fase_directo_C22 = fase_directo_C22 + " horas";
  htmlTemplate.fase_directo_D22 = (fase_directo_D22*100).toFixed(2) + " %";
  htmlTemplate.fase_autonomo_E22 = fase_autonomo_E22 + " horas";
  htmlTemplate.fase_autonomo_F22 = (fase_autonomo_F22*100).toFixed(2) + " %";

  // ------------------------------------------------------------------------------------------------------

  // TIPO DE COMPETENCIA

  // Directo

  const comp_directo_C46 = time.getRange('C46').getValue();
  const comp_directo_C47 = time.getRange('C47').getValue();
  const comp_directo_C48 = time.getRange('C48').getValue();
  const comp_directo_C49 = time.getRange('D49').getValue();

  htmlTemplate.comp_directo_C46 = comp_directo_C46 + " horas";
  htmlTemplate.comp_directo_C47 = comp_directo_C47 + " horas";
  htmlTemplate.comp_directo_C48 = comp_directo_C48 + " horas";
  htmlTemplate.comp_directo_C49 = comp_directo_C49 + " horas";

  const comp_directo_D46 = time.getRange('D46').getValue();
  const comp_directo_D47 = time.getRange('D47').getValue();
  const comp_directo_D48 = time.getRange('D48').getValue();
  const comp_directo_D49 = time.getRange('D49').getValue();

  htmlTemplate.comp_directo_D46 = (comp_directo_D46*100).toFixed(2) + " %";
  htmlTemplate.comp_directo_D47 = (comp_directo_D47*100).toFixed(2) + " %";
  htmlTemplate.comp_directo_D48 = (comp_directo_D48*100).toFixed(2) + " %";
  htmlTemplate.comp_directo_D49 = (comp_directo_D49*100).toFixed(2) + " %";

  // Autonomo

  const comp_autonomo_E46 = time.getRange('E46').getValue();
  const comp_autonomo_E47 = time.getRange('E47').getValue();
  const comp_autonomo_E48 = time.getRange('E48').getValue();
  const comp_autonomo_E49 = time.getRange('E49').getValue();

  htmlTemplate.comp_autonomo_E46 = comp_autonomo_E46 + " horas";
  htmlTemplate.comp_autonomo_E47 = comp_autonomo_E47 + " horas";
  htmlTemplate.comp_autonomo_E48 = comp_autonomo_E48 + " horas";
  htmlTemplate.comp_autonomo_E49 = comp_autonomo_E49 + " horas";

  const comp_autonomo_F46 = time.getRange('F46').getValue();
  const comp_autonomo_F47 = time.getRange('F47').getValue();
  const comp_autonomo_F48 = time.getRange('F48').getValue();
  const comp_autonomo_F49 = time.getRange('F49').getValue();

  htmlTemplate.comp_autonomo_F46 = (comp_autonomo_F46*100).toFixed(2) + " %";
  htmlTemplate.comp_autonomo_F47 = (comp_autonomo_F47*100).toFixed(2) + " %";
  htmlTemplate.comp_autonomo_F48 = (comp_autonomo_F48*100).toFixed(2) + " %";
  htmlTemplate.comp_autonomo_F49 = (comp_autonomo_F49*100).toFixed(2) + " %";

  // Totales

  const comp_totales_G46 = time.getRange('G46').getValue();
  const comp_totales_G47 = time.getRange('G47').getValue();
  const comp_totales_G48 = time.getRange('G48').getValue();
  const comp_totales_G49 = time.getRange('G49').getValue();

  htmlTemplate.comp_totales_G46 = comp_totales_G46 + " horas";
  htmlTemplate.comp_totales_G47 = comp_totales_G47 + " horas";
  htmlTemplate.comp_totales_G48 = comp_totales_G48 + " horas";
  htmlTemplate.comp_totales_G49 = comp_totales_G49 + " horas";

  const comp_totales_H46 = time.getRange('H46').getValue();
  const comp_totales_H47 = time.getRange('H47').getValue();
  const comp_totales_H48 = time.getRange('H48').getValue();
  const comp_totales_H49 = time.getRange('H49').getValue();

  htmlTemplate.comp_totales_H46 = (comp_totales_H46*100).toFixed(2) + " %";
  htmlTemplate.comp_totales_H47 = (comp_totales_H47*100).toFixed(2) + " %";
  htmlTemplate.comp_totales_H48 = (comp_totales_H48*100).toFixed(2) + " %";
  htmlTemplate.comp_totales_H49 = (comp_totales_H49*100).toFixed(2) + " %";

  // TIPO DE EVIDENCIA

  // Conocimiento
  const cono_directo_C73 = time.getRange('C73').getValue();
  const cono_autonomo_E73 = time.getRange('E73').getValue();

  htmlTemplate.cono_directo_C73 = cono_directo_C73 + " horas";
  htmlTemplate.cono_autonomo_E73 = cono_autonomo_E73 + " horas";

  // % Conocimiento
  const cono_directo_D73 = time.getRange('D73').getValue();
  const cono_autonomo_F73 = time.getRange('F73').getValue();

  htmlTemplate.cono_directo_D73 = (cono_directo_D73*100).toFixed(2) + " %";
  htmlTemplate.cono_autonomo_F73 = (cono_autonomo_F73*100).toFixed(2) + " %";

   // Evidencia

  const evid_directo_C74 = time.getRange('C74').getValue();
  const evid_autonomo_E74 = time.getRange('E74').getValue();

  htmlTemplate.evid_directo_C74 = evid_directo_C74 + " horas";
  htmlTemplate.evid_autonomo_E74 = evid_autonomo_E74 + " horas";

  // % Evidencia

  const evid_directo_D74 = time.getRange('D74').getValue();
  const evid_autonomo_F74 = time.getRange('F74').getValue();

  htmlTemplate.evid_directo_D74 = (evid_directo_D74*100).toFixed(2) + " %";
  htmlTemplate.evid_autonomo_F74 = (evid_autonomo_F74*100).toFixed(2) + " %";

    // Totales

  const cono_totales_G73 = time.getRange('G73').getValue();
  const evid_totales_G74 = time.getRange('G74').getValue();

  htmlTemplate.cono_totales_G73 = cono_totales_G73 + " horas";
  htmlTemplate.evid_totales_G74 = evid_totales_G74 + " horas";

  const cono_totales_H73 = time.getRange('H73').getValue();
  const evid_totales_H74 = time.getRange('H74').getValue();

  htmlTemplate.cono_totales_H73 = (cono_totales_H73*100).toFixed(2) + " %";
  htmlTemplate.evid_totales_H74 = (evid_totales_H74*100).toFixed(2) + " %";

  // ------------------------------------------------------------------------------------------------------

  // COMPETENCIA

  // Supervisión en el funcionamiento
  const comp_cod_A189 = time.getRange('A189').getValue();
  const comp_desc_B189 = time.getRange('B189').getValue();
  const comp_valor_C189 = time.getRange('C189').getValue();
  const comp_porcentaje_D189 = time.getRange('D189').getValue();
  const comp_valor_E189 = time.getRange('E189').getValue();
  const comp_porcentaje_F189 = time.getRange('F189').getValue();
  const comp_valor_G189 = time.getRange('G189').getValue();
  const comp_porcentaje_H189 = time.getRange('H189').getValue();

  htmlTemplate.comp_cod_A189 = comp_cod_A189;
  htmlTemplate.comp_desc_B189 = comp_desc_B189;
  htmlTemplate.comp_valor_C189 = comp_valor_C189 + " horas";
  htmlTemplate.comp_porcentaje_D189 = (comp_porcentaje_D189*100).toFixed(2);+ " %";
  htmlTemplate.comp_valor_E189 = comp_valor_E189 + " horas";
  htmlTemplate.comp_porcentaje_F189 = (comp_porcentaje_F189*100).toFixed(2) + " %";
  htmlTemplate.comp_valor_G189 = comp_valor_G189 + " horas";
  htmlTemplate.comp_porcentaje_H189 = (comp_porcentaje_H189*100).toFixed(2) + " %";

  // Recolección de Muestras  

  const comp_cod_A190 = time.getRange('A190').getValue();
  const comp_desc_B190 = time.getRange('B190').getValue();
  const comp_valor_C190 = time.getRange('C190').getValue();
  const comp_porcentaje_D190 = time.getRange('D190').getValue();
  const comp_valor_E190 = time.getRange('E190').getValue();
  const comp_porcentaje_F190 = time.getRange('F190').getValue();
  const comp_valor_G190 = time.getRange('G190').getValue();
  const comp_porcentaje_H190 = time.getRange('H190').getValue();

  htmlTemplate.comp_cod_A190 = comp_cod_A190;
  htmlTemplate.comp_desc_B190 = comp_desc_B190;
  htmlTemplate.comp_valor_C190 = comp_valor_C190 + " horas";
  htmlTemplate.comp_porcentaje_D190 = (comp_porcentaje_D190*100).toFixed(2)+ " %";
  htmlTemplate.comp_valor_E190 = comp_valor_E190 + " horas";
  htmlTemplate.comp_porcentaje_F190 = (comp_porcentaje_F190*100).toFixed(2) + " %";
  htmlTemplate.comp_valor_G190 = comp_valor_G190 + " horas";
  htmlTemplate.comp_porcentaje_H190 = (comp_porcentaje_H190*100).toFixed(2) + " %";

  // Ingles

  const comp_cod_A191 = time.getRange('A191').getValue();
  const comp_desc_B191 = time.getRange('B191').getValue();
  const comp_valor_C191 = time.getRange('C191').getValue();
  const comp_porcentaje_D191 = time.getRange('D191').getValue();
  const comp_valor_E191 = time.getRange('E191').getValue();
  const comp_porcentaje_F191 = time.getRange('F191').getValue();
  const comp_valor_G191 = time.getRange('G191').getValue();
  const comp_porcentaje_H191 = time.getRange('H191').getValue();

  htmlTemplate.comp_cod_A191 = comp_cod_A191;
  htmlTemplate.comp_desc_B191 = comp_desc_B191;
  htmlTemplate.comp_valor_C191 = comp_valor_C191 + " horas";
  htmlTemplate.comp_porcentaje_D191 = (comp_porcentaje_D191*100).toFixed(2)+ " %";
  htmlTemplate.comp_valor_E191 = comp_valor_E191 + " horas";
  htmlTemplate.comp_porcentaje_F191 = (comp_porcentaje_F191*100).toFixed(2) + " %";
  htmlTemplate.comp_valor_G191 = comp_valor_G191 + " horas";
  htmlTemplate.comp_porcentaje_H191 = (comp_porcentaje_H191*100).toFixed(2) + " %";

 // Matemáticas

  const comp_cod_A192 = time.getRange('A192').getValue();
  const comp_desc_B192 = time.getRange('B192').getValue();
  const comp_valor_C192 = time.getRange('C192').getValue();
  const comp_porcentaje_D192 = time.getRange('D192').getValue();
  const comp_valor_E192 = time.getRange('E192').getValue();
  const comp_porcentaje_F192 = time.getRange('F192').getValue();
  const comp_valor_G192 = time.getRange('G192').getValue();
  const comp_porcentaje_H192 = time.getRange('H192').getValue();

  htmlTemplate.comp_cod_A192 = comp_cod_A192;
  htmlTemplate.comp_desc_B192 = comp_desc_B192;
  htmlTemplate.comp_valor_C192 = comp_valor_C192 + " horas";
  htmlTemplate.comp_porcentaje_D192 = (comp_porcentaje_D192*100).toFixed(2) + " %";
  htmlTemplate.comp_valor_E192 = comp_valor_E192 + " horas";
  htmlTemplate.comp_porcentaje_F192 = (comp_porcentaje_F192*100).toFixed(2) + " %";
  htmlTemplate.comp_valor_G192 = comp_valor_G192 + " horas";
  htmlTemplate.comp_porcentaje_H192 = (comp_porcentaje_H192*100).toFixed(2) + " %";

  // Biologia

  const comp_cod_A193 = time.getRange('A193').getValue();
  const comp_desc_B193 = time.getRange('B193').getValue();
  const comp_valor_C193 = time.getRange('C193').getValue();
  const comp_porcentaje_D193 = time.getRange('D193').getValue();
  const comp_valor_E193 = time.getRange('E193').getValue();
  const comp_porcentaje_F193 = time.getRange('F193').getValue();
  const comp_valor_G193 = time.getRange('G193').getValue();
  const comp_porcentaje_H193 = time.getRange('H193').getValue();

  htmlTemplate.comp_cod_A193 = comp_cod_A193;
  htmlTemplate.comp_desc_B193 = comp_desc_B193;
  htmlTemplate.comp_valor_C193 = comp_valor_C193 + " horas";
  htmlTemplate.comp_porcentaje_D193 = (comp_porcentaje_D193*100).toFixed(2)+ " %";
  htmlTemplate.comp_valor_E193 = comp_valor_E193 + " horas";
  htmlTemplate.comp_porcentaje_F193 = (comp_porcentaje_F193*100).toFixed(2) + " %";
  htmlTemplate.comp_valor_G193 = comp_valor_G193 + " horas";
  htmlTemplate.comp_porcentaje_H193 = (comp_porcentaje_H193*100).toFixed(2) + " %";

   // Comunicación

  const comp_cod_A194 = time.getRange('A194').getValue();
  const comp_desc_B194 = time.getRange('B194').getValue();
  const comp_valor_C194 = time.getRange('C194').getValue();
  const comp_porcentaje_D194 = time.getRange('D194').getValue();
  const comp_valor_E194 = time.getRange('E194').getValue();
  const comp_porcentaje_F194 = time.getRange('F194').getValue();
  const comp_valor_G194 = time.getRange('G194').getValue();
  const comp_porcentaje_H194 = time.getRange('H194').getValue();

  htmlTemplate.comp_cod_A194 = comp_cod_A194;
  htmlTemplate.comp_desc_B194 = comp_desc_B194;
  htmlTemplate.comp_valor_C194 = comp_valor_C194 + " horas";
  htmlTemplate.comp_porcentaje_D194 = (comp_porcentaje_D194*100).toFixed(2)+ " %";
  htmlTemplate.comp_valor_E194 = comp_valor_E194 + " horas";
  htmlTemplate.comp_porcentaje_F194 = (comp_porcentaje_F194*100).toFixed(2) + " %";
  htmlTemplate.comp_valor_G194 = comp_valor_G194 + " horas";
  htmlTemplate.comp_porcentaje_H194 = (comp_porcentaje_H194*100).toFixed(2) + " %";

// Logistica Costos e Inventarios
  const comp_cod_A195 = time.getRange('A195').getValue();
  const comp_desc_B195 = time.getRange('B195').getValue();
  const comp_valor_C195 = time.getRange('C195').getValue();
  const comp_porcentaje_D195 = time.getRange('D195').getValue();
  const comp_valor_E195 = time.getRange('E195').getValue();
  const comp_porcentaje_F195 = time.getRange('F195').getValue();
  const comp_valor_G195 = time.getRange('G195').getValue();
  const comp_porcentaje_H195 = time.getRange('H195').getValue();

  htmlTemplate.comp_cod_A195 = comp_cod_A195;
  htmlTemplate.comp_desc_B195 = comp_desc_B195;
  htmlTemplate.comp_valor_C195 = comp_valor_C195 + " horas";
  htmlTemplate.comp_porcentaje_D195 = (comp_porcentaje_D195*100).toFixed(2)+ " %";
  htmlTemplate.comp_valor_E195 = comp_valor_E195 + " horas";
  htmlTemplate.comp_porcentaje_F195 = (comp_porcentaje_F195*100).toFixed(2) + " %";
  htmlTemplate.comp_valor_G195 = comp_valor_G195 + " horas";
  htmlTemplate.comp_porcentaje_H195 = (comp_porcentaje_H195*100).toFixed(2) + " %";


  // ========================================================================================================
  // CONFIGURACIÓN

  const htmlForEmail = htmlTemplate.evaluate().getContent();
  console.log(htmlForEmail);

  var destinatarios = 'dfosorio@sena.edu.co';
  GmailApp.sendEmail(destinatarios, 'SENA | CDHC | SSA&S | GUIA APRENDIZAJE 1/7', 'Guía de Aprendizaje No. 1/7 - En Construcción', {htmlBody: htmlForEmail});
  }