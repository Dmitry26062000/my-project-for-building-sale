
function outtrue(){
if(confirm('Вы хотите выйти из своего аккаунта?')){
    window.location.href="/auth/"
}
else{
    alert('Хорошо!')
}
 console.log('Yeap')
}