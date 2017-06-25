-- Necessário:
scriptId         = "edu.cefet.ger.myo.myfirstscript"
scriptTitle      = "Script de Teste"
scriptDetailsUrl = ""
 
appTitle = ""
 
 
-- Chamado quando for necessário saber o nome
-- do aplicativo em foco:
function activeAppName()
    return appTitle
end
 
-- Chamado toda vez que um programa estiver em foco:
function onForegroundWindowChange(app, title)
-- Seleciona o braço ("left"/"right"):
   braco = myo.getArm()
 
   appTitle = title
    return true
end
 
-- Chamado em cada mudança de poses:
function onPoseEdge(pose, edge)
 
-- Se é uma das poses estabelecidas:
   if(pose ~= "rest" and pose ~= "unknown") then
 
   -- Se não há mudança de estados (edge == off),
   -- o Myo deve ser travado após um tempo
      estado = (edge == "off") and "timed" or "hold"
    end
 
-- Se há mudança de estados, então verifica condição
-- de travamento do Myo:
    if (edge == "on") then
           myo.unlock(estado)
           menuPose(pose)
    end
 
end
 
function menuPose(pose)
   if (pose == "waveOut") then
       onWaveOut()
    elseif (pose == "waveIn") then
        onWaveIn()
    elseif (pose == "fingersSpread") then
        onFingersSpread()
    end
end
 
function onWaveOut()
    myo.vibrate("short")
    if(braco == "right") then
       myo.debug("Direita")
    else
       myo.debug("Esquerda")
    end
end
 
function onWaveIn()
    myo.vibrate("short")
    if(braco == "left") then
       myo.debug("Direita")
    else
       myo.debug("Esquerda")
    end
end
