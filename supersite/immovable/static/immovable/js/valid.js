let c=0;
    let ans=prompt('Введите пароль:' );
    while(ans!=='admin'){
        let ans=prompt('Введите пароль:' );
        if (ans==='admin'){
            alert('Добро пожаловать!');
            break;
        }
        else {
            c++;
            if (c===2) {
                alert('Вы ввели не верный пароль несколько раз!');
                window.location.href = "/auth/"
                break;
            }
        }
    }