 
 ​
  
 ​def​ ​destroy​(​direction​): 
  
 ​    ​if​ ​direction​==​"LD"​: 
 ​        ​global​ ​mid 
 ​        ​game​[​size​-​1​][​mid​]​=​"G" 
 ​        ​mid​=​mid​-​1 
 ​        ​game​[​size​-​1​][​mid​]​=​"
​direction​==​"RD"​: 
 ​        ​game​[​size​-​1​][​mid​]​=​"G" 
 ​        ​mid​=​mid​+​1 
 ​        ​game​[​size​-​1​][​mid​]​=​"o" 
 ​    ​else​: 
 ​        ​print​(​"ST"​) 
  
 ​    ​for​ ​x​ ​in​ ​range​(​size​-​2​,​0​,​-​1​): 
 ​            ​print​(​"hello"​) 
 ​            ​if​ ​game​[​x​][​mid​]​!=​" "​: 
 ​                    ​if​ ​game​[​x​][​mid​]​==​"1"​: 
 ​                         ​game​[​x​][​mid​]​=​" " 
 ​                         ​break 
 ​                    ​else​: 
 ​                         ​game​[​x​][​mid​]​=​str​(​int​(​game​[​x​][​mid​])​-​1​) 
 ​                         ​break​    
  
  
  
 ​def​ ​printmat​(): 
 ​    ​for​ ​i​ ​in​ ​range​(​0​,​size​): 
 ​         ​row​=​"" 
 ​         ​for​ ​j​ ​in​ ​range​(​0​,​size​): 
 ​             ​chart​=​str​(​game​[​i​][​j​]) 
 ​             ​row​=​row​+​chart 
 ​         ​print​(​row​)     
  
  
  
 ​while​ ​True​: 
  
 ​    ​if​ ​input​(​'Do you want to add bricks? Y/N :  '​) ​==​ ​'n'​: 
 ​        ​printmat​() 
 ​        ​break 
 ​    ​else​: 
  
 ​         ​position​=​input​(​"Enter the brick's position and the brick type : "​) 
 ​         ​brick​(​position​) 
  
  
 ​ballcount​=​input​(​"Enter ball count :  "​) 
 ​ballcount​=​int​(​ballcount​) 
  
  
 ​while​ ​True​: 
  
 ​    ​if​ ​input​(​'Do you want to traverse the ball ? Y/N :  '​) ​==​ ​'n'​: 
 ​        ​printmat​() 
 ​        ​break 
 ​    ​else​: 
 ​         ​balldir​=​input​(​"Enter the direction in which the ball need to traverse : "​)     
 ​         ​destroy​​)  
 ​         ​ballcount​=​ballcount​-​1 
 ​         ​printmat​() 

 
