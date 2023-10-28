# Superheroes-App

![Ekran görüntüsü 2023-10-28 173717](https://github.com/KaganMuslu/Superheroes-App/assets/71410113/2169578f-4251-4c3b-a0f8-f3fce8649be2)

Projenin amacı, kullanıcılara Süperkahramanlar koleksiyonunu keşfetme ve kendi istedikleri kahraman koleksiyonunu oluşturma fırsatı sunmaktır. Kullanıcılar, uygulama aracılığıyla istedikleri kahramanları edinebilir, kendi koleksiyonlarını oluşturabilir ve bu süperkahramanlar hakkında detaylı bilgilere erişebilirler.

Proje, kullanıcıların siteye giriş yapabileceği veya yeni hesap oluşturabileceği bir kullanıcı giriş ve kayıt olma sistemi içermektedir. Bu sayede kullanıcılar kendi profillerini oluşturabilir, koleksiyonlarını kaydedebilir ve istedikleri kahramanları seçebilirler.

Site üzerinde, belli aralıklarla 2 yeni rastgele kahraman eklenen dinamik bir koleksiyon sayfası bulunmaktadır. Kullanıcılar bu sayede 600'e yakın kahramandan sürekli olarak yeni kahramanları keşfedebilirler.

Ayrıca kullanıcılar, site üzerinde her kahramanın detaylı özelliklerine de erişilebilir. Kahramanların isimleri, cinsiyetleri, ırkları, boyutları, kiloları, göz renkleri, saç renkleri, ikincil kimlikleri, takma adları, doğum yerleri, ilk görünüşleri gibi birçok özellik bulunmaktadır.

Proje, verileri önce bir <a href="https://superheroapi.com">SuperHero API</a>'den çekerek başlar ve daha sonra bu verileri kendi <a href="https://www.postgresql.org">PostgreSQL</a> veritabanına aktararak kullanıcıların daha hızlı ve güvenilir bir deneyim yaşamalarını sağlar. Bu veritabanı sayesinde kullanıcıların koleksiyonları ve diğer bilgiler güvenli bir şekilde saklanır.

Frontend tarafında <a href="https://www.w3schools.com/html/html_css.asp">HTML, CSS</a> ve <a href="https://getbootstrap.com/docs/5.2/getting-started/introduction/">Bootstrap 5</a> kullanılmıştır, bu sayede kullanıcılar kolayca gezinebilirler. Projenin backend kısmı <a href="https://flask.palletsprojects.com">Flask frameworkü</a> kullanılarak geliştirilmiştir. <a href="https://flask-login.readthedocs.io/en/latest/">Flask-Login</a> ve <a href="https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/">Flask-SQLAlchemy</a> kütüphaneleri kullanılarak kullanıcı giriş-çıkış işlemleri ve veritabanı yönetimi kolaylıkla gerçekleştirilir.

Proje, <a href="https://vercel.com">Vercel</a>'de ücretsiz hosting hizmeti ile canlıya alınmış ve <a href="https://www.postgresql.org">PostgreSQL</a> veritabanı da ücretsiz olarak Render.com üzerinde barındırılmıştır. Bu sayede kullanıcılar herhangi bir ücret ödemeden uygulamayı kullanabilirler.

Projenin amacı, süperkahraman koleksiyonlarına ilgi duyan herkesin bu dünyayı keşfetmesine ve kendi özel koleksiyonlarını oluşturmasına olanak sağlamaktır.

![Ekran görüntüsü 2023-10-26 164558](https://github.com/KaganMuslu/Superheroes-App/assets/71410113/7bd68570-b9e6-4a10-8cd5-a44ec842cfed)
