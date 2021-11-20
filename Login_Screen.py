Username = 'admin'
Password = 'admin'
kullanıcı = input('İsim:')
password = input('Şifre:')
if Username == kullanıcı and Password != password :
    print('Kullanıcı adınız doğru Şifreniz yanlıştır lütfen tekrar deneyiniz.')
if Username != kullanıcı and Password == password :
    print('Şifreniz Doğru Kullanıcı adınız yanlıştır lütfen tekrar deneyiniz.'),
if Username == kullanıcı and Password == password :
    print('Giriş Başarılı')