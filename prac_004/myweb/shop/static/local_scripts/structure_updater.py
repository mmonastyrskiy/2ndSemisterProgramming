import os
import configparser as config
from tqdm import tqdm
import mysql.connector as conn

CategoryHTML = ""
currency_code = u'\u20bd'




def BuildCategroyCard(record: list) -> str:
    global image_folder
    global productHTMLs_folder
    global currency_code
    global image_folder
    product_id = record[0]
    product_art = record[1]
    product_name = record[2]
    product_price = record[3]
    product_brand = record[4]
    product_category = record[5]
    product_original_link = record[6]
    product_description = record[7]

    for path,directory,names in os.walk(image_folder):
    	for file in names:
    		if str(product_id) == file.split(".")[0]:
    			img_path = os.path.join(path,file)

    personal_page = os.path.join(productHTMLs_folder, str(product_id) + ".html")

    template = f"""
	<div class="col-md-6 col-lg-4">
                <div class="card text-center card-product">
                  <div class="card-product__img">
                    <img class="card-img" src="{img_path}" alt="">
                    <ul class="card-product__imgOverlay">
                      <li><button><i class="ti-search"></i></button></li>
                      <li><button><i class="ti-shopping-cart"></i></button></li>
                      <li><button><i class="ti-heart"></i></button></li>
                    </ul>
                  </div>
                  <div class="card-body">
                    <p>{product_category}</p>
                    <h4 class="card-product__title"><a href="{personal_page}">{product_name}</a></h4>
                    <p class="card-product__price">{product_price}{currency_code}</p>
                  </div> 
                </div>
              </div>

	"""
    return template


def BuildStaticProductPage(record: list) -> None:
    global image_folder
    global vendors_folder
    global productHTMLs_folder
    global base_folder
    global currency_code
    product_id = record[0]
    print(product_id)
    product_art = record[1]
    product_name = record[2]
    product_price = record[3]
    product_brand = record[4]
    product_category = record[5]
    product_original_link = record[6]
    product_description = record[7]
    for path,directory,names in os.walk(image_folder):
    	for file in names:
    		if str(product_id) == file.split(".")[0]:
    			img_path = os.path.join(path,file)

    template = f"""
	<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Твой Девайс - {product_name}</title>
	<link rel="icon" href="{base_folder}/img/Fevicon.png" type="image/png">
  <link rel="stylesheet" href="{vendors_folder}/bootstrap/bootstrap.min.css">
  <link rel="stylesheet" href="{vendors_folder}/fontawesome/css/all.min.css">
	<link rel="stylesheet" href="{vendors_folder}/themify-icons/themify-icons.css">
	<link rel="stylesheet" href="{vendors_folder}/linericon/style.css">
  <link rel="stylesheet" href="{vendors_folder}/nice-select/nice-select.css">
  <link rel="stylesheet" href="{vendors_folder}/owl-carousel/owl.theme.default.min.css">
  <link rel="stylesheet" href="{vendors_folder}/owl-carousel/owl.carousel.min.css">

  <link rel="stylesheet" href="{base_folder}/css/style.css">
</head>
<body>
	<!--================ Start Header Menu Area =================-->
		<header class="header_area">
    <div class="main_menu">
      <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container">
          <a class="navbar-brand logo_h" href="index.html"><img src="{base_folder}/img/logo.png" alt=""></a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <div class="collapse navbar-collapse offset" id="navbarSupportedContent">
            <ul class="nav navbar-nav menu_nav ml-auto mr-auto">
              <li class="nav-item"><a class="nav-link" href="{base_folder}/index.html">Домой</a></li>
              <li class="nav-item active submenu dropdown">
                <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                  aria-expanded="false">Магазин</a>
                <ul class="dropdown-menu">
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/category.html">Категории магазиновy</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/single-product.html">Детали продукта</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/checkout.html">Оформление</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/confirmation.html">Подтверждение</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/cart.html">Корзина</a></li>
                </ul>
							</li>
              <li class="nav-item submenu dropdown">
                <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                  aria-expanded="false">Блог</a>
                <ul class="dropdown-menu">
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/blog.html">Блог</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/register.html">Регистрация</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/single-blog.html">Детали</a></li>
                </ul>
							</li>
							<li class="nav-item submenu dropdown">
                <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                  aria-expanded="false">Страницы</a>
                <ul class="dropdown-menu">
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/login.html">Логин</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/tracking-order.html">Отслеживание</a></li>
                </ul>
              </li>
              <li class="nav-item"><a class="nav-link" href="contact.html">Контакты</a></li>
            </ul>

            <ul class="nav-shop">
              <li class="nav-item"><button><i class="ti-search"></i></button></li>
              <li class="nav-item"><button><i class="ti-shopping-cart"></i><span class="nav-shop__circle">3</span></button> </li>
              <li class="nav-item"><a class="button button-header" href="#">Купить сейчас</a></li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </header>
	<!--================ End Header Menu Area =================-->

	<!-- ================ start banner area ================= -->	
	<section class="blog-banner-area" id="blog">
		<div class="container h-100">
			<div class="blog-banner">
				<div class="text-center">
					<h1>Shop Single</h1>
					<nav aria-label="breadcrumb" class="banner-breadcrumb">
            <ol class="breadcrumb">
              <li class="breadcrumb-item"><a href="#">Home</a></li>
              <li class="breadcrumb-item active" aria-current="page">Shop Single</li>
            </ol>
          </nav>
				</div>
			</div>
    </div>
	</section>
	<!-- ================ end banner area ================= -->


  <!--================Single Product Area =================-->
	<div class="product_image_area">
		<div class="container">
			<div class="row s_product_inner">
				<div class="col-lg-6">
					<div class="owl-carousel owl-theme s_Product_carousel">
						<div class="single-prd-item">
							<img class="img-fluid" src="{img_path}" alt="">
						</div>
						<!-- <div class="single-prd-item">
							<img class="img-fluid" src="{img_path}" alt="">
						</div>
						<div class="single-prd-item">
							<img class="img-fluid" src="{img_path}" alt="">
						</div> -->
					</div>
				</div>
				<div class="col-lg-5 offset-lg-1">
					<div class="s_product_text">
						<h3>{product_name} By {product_brand}</h3>
						<h2>{product_price + currency_code}</h2>
						<ul class="list">
							<li><a class="active" href="#"><span>Category</span> : {product_category}</a></li>
							<li><a href="#"><span>Availibility</span> : На складе</a></li>
						</ul>
						{product_description}
						<div class="product_count">
              <label for="qty">Кол-во:</label>
              <button onclick="var result = document.getElementById('sst'); var sst = result.value; if( !isNaN( sst )) result.value++;return false;"
							 class="increase items-count" type="button"><i class="ti-angle-left"></i></button>
							<input type="text" name="qty" id="sst" size="2" maxlength="12" value="1" title="Количество:" class="input-text qty">
							<button onclick="var result = document.getElementById('sst'); var sst = result.value; if( !isNaN( sst ) &amp;&amp; sst > 0 ) result.value--;return false;"
               class="reduced items-count" type="button"><i class="ti-angle-right"></i></button>
							<a class="button primary-btn" href="#">Add to Cart</a>               
						</div>
						<div class="card_area d-flex align-items-center">
							<a class="icon_btn" href="#"><i class="lnr lnr lnr-diamond"></i></a>
							<a class="icon_btn" href="#"><i class="lnr lnr lnr-heart"></i></a>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
	<!--================End Single Product Area =================-->

	<!--================Product Description Area =================-->
	<section class="product_description_area">
		<div class="container">
			<ul class="nav nav-tabs" id="myTab" role="tablist">
				<li class="nav-item">
					<a class="nav-link" id="home-tab" data-toggle="tab" href="#home" role="tab" aria-controls="home" aria-selected="true">Описание</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" id="profile-tab" data-toggle="tab" href="#profile" role="tab" aria-controls="profile"
					 aria-selected="false">Характеристики</a>
				</li>
				<li class="nav-item">
					<a class="nav-link" id="contact-tab" data-toggle="tab" href="#contact" role="tab" aria-controls="contact"
					 aria-selected="false">Коментарии</a>
				</li>
				<li class="nav-item">
					<a class="nav-link active" id="review-tab" data-toggle="tab" href="#review" role="tab" aria-controls="review"
					 aria-selected="false">Обзоры</a>
				</li>
			</ul>
			<div class="tab-content" id="myTabContent">
				<div class="tab-pane fade" id="home" role="tabpanel" aria-labelledby="home-tab">
					{product_description}
				</div>
				<div class="tab-pane fade" id="profile" role="tabpanel" aria-labelledby="profile-tab">
					<div class="table-responsive">
					</div>
				</div>
				<div class="tab-pane fade" id="contact" role="tabpanel" aria-labelledby="contact-tab">
					<div class="row">
						<div class="col-lg-6">
							<div class="comment_list">
								<div class="review_item">
									<div class="media">
										<div class="d-flex">
											<img src="{base_folder}/img/product/review-1.png" alt="">
										</div>
										<div class="media-body">
											<h4>Blake Ruiz</h4>
											<h5>12th Feb, 2018 at 05:56 pm</h5>
											<a class="reply_btn" href="#">ответ</a>
										</div>
									</div>
									<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et
										dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
										commodo</p>
								</div>
								<div class="review_item reply">
									<div class="media">
										<div class="d-flex">
											<img src="img/product/review-2.png" alt="">
										</div>
										<div class="media-body">
											<h4>Blake Ruiz</h4>
											<h5>12th Feb, 2018 at 05:56 pm</h5>
											<a class="reply_btn" href="#">Reply</a>
										</div>
									</div>
									<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et
										dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
										commodo</p>
								</div>
								<div class="review_item">
									<div class="media">
										<div class="d-flex">
											<img src="{base_folder}/img/product/review-3.png" alt="">
										</div>
										<div class="media-body">
											<h4>Blake Ruiz</h4>
											<h5>12th Feb, 2018 at 05:56 pm</h5>
											<a class="reply_btn" href="#">Reply</a>
										</div>
									</div>
									<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et
										dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
										commodo</p>
								</div>
							</div>
						</div>
						<div class="col-lg-6">
							<div class="review_box">
								<h4>Написать комментарий</h4>
								<form class="row contact_form" action="contact_process.php" method="post" id="contactForm" novalidate="novalidate">
									<div class="col-md-12">
										<div class="form-group">
											<input type="text" class="form-control" id="name" name="name" placeholder="Ваше имя">
										</div>
									</div>
									<div class="col-md-12">
										<div class="form-group">
											<input type="email" class="form-control" id="email" name="email" placeholder="Email">
										</div>
									</div>
									<div class="col-md-12">
										<div class="form-group">
											<input type="text" class="form-control" id="number" name="number" placeholder="Телефон">
										</div>
									</div>
									<div class="col-md-12">
										<div class="form-group">
											<textarea class="form-control" name="message" id="message" rows="1" placeholder="Сообщение"></textarea>
										</div>
									</div>
									<div class="col-md-12 text-right">
										<button type="submit" value="submit" class="btn primary-btn">Подтвердить</button>
									</div>
								</form>
							</div>
						</div>
					</div>
				</div>
				<div class="tab-pane fade show active" id="review" role="tabpanel" aria-labelledby="review-tab">
					<div class="row">
						<div class="col-lg-6">
							<div class="row total_rate">
								<div class="col-6">
									<div class="box_total">
										<h5>Overall</h5>
										<h4>4.0</h4>
										<h6>(03 Reviews)</h6>
									</div>
								</div>
								<div class="col-6">
									<div class="rating_list">
										<h3>Based on 3 Reviews</h3>
										<ul class="list">
											<li><a href="#">5 Star <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i
													 class="fa fa-star"></i><i class="fa fa-star"></i> 01</a></li>
											<li><a href="#">4 Star <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i
													 class="fa fa-star"></i><i class="fa fa-star"></i> 01</a></li>
											<li><a href="#">3 Star <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i
													 class="fa fa-star"></i><i class="fa fa-star"></i> 01</a></li>
											<li><a href="#">2 Star <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i
													 class="fa fa-star"></i><i class="fa fa-star"></i> 01</a></li>
											<li><a href="#">1 Star <i class="fa fa-star"></i><i class="fa fa-star"></i><i class="fa fa-star"></i><i
													 class="fa fa-star"></i><i class="fa fa-star"></i> 01</a></li>
										</ul>
									</div>
								</div>
							</div>
							<div class="review_list">
								<div class="review_item">
									<div class="media">
										<div class="d-flex">
											<img src="{base_folder}/img/product/review-1.png" alt="">
										</div>
										<div class="media-body">
											<h4>Blake Ruiz</h4>
											<i class="fa fa-star"></i>
											<i class="fa fa-star"></i>
											<i class="fa fa-star"></i>
											<i class="fa fa-star"></i>
											<i class="fa fa-star"></i>
										</div>
									</div>
									<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et
										dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
										commodo</p>
								</div>
								<div class="review_item">
									<div class="media">
										<div class="d-flex">
											<img src="{base_folder}/img/product/review-2.png" alt="">
										</div>
										<div class="media-body">
											<h4>Blake Ruiz</h4>
											<i class="fa fa-star"></i>
											<i class="fa fa-star"></i>
											<i class="fa fa-star"></i>
											<i class="fa fa-star"></i>
											<i class="fa fa-star"></i>
										</div>
									</div>
									<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et
										dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
										commodo</p>
								</div>
								<div class="review_item">
									<div class="media">
										<div class="d-flex">
											<img src="{base_folder}/img/product/review-3.png" alt="">
										</div>
										<div class="media-body">
											<h4>Blake Ruiz</h4>
											<i class="fa fa-star"></i>
											<i class="fa fa-star"></i>
											<i class="fa fa-star"></i>
											<i class="fa fa-star"></i>
											<i class="fa fa-star"></i>
										</div>
									</div>
									<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et
										dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
										commodo</p>
								</div>
							</div>
						</div>
						<div class="col-lg-6">
							<div class="review_box">
								<h4>Add a Review</h4>
								<p>Your Rating:</p>
								<ul class="list">
									<li><a href="#"><i class="fa fa-star"></i></a></li>
									<li><a href="#"><i class="fa fa-star"></i></a></li>
									<li><a href="#"><i class="fa fa-star"></i></a></li>
									<li><a href="#"><i class="fa fa-star"></i></a></li>
									<li><a href="#"><i class="fa fa-star"></i></a></li>
								</ul>
								<p>Outstanding</p>
                <form action="#/" class="form-contact form-review mt-3">
                  <div class="form-group">
                    <input class="form-control" name="name" type="text" placeholder="Enter your name" required>
                  </div>
                  <div class="form-group">
                    <input class="form-control" name="email" type="email" placeholder="Enter email address" required>
                  </div>
                  <div class="form-group">
                    <input class="form-control" name="subject" type="text" placeholder="Enter Subject">
                  </div>
                  <div class="form-group">
                    <textarea class="form-control different-control w-100" name="textarea" id="textarea" cols="30" rows="5" placeholder="Enter Message"></textarea>
                  </div>
                  <div class="form-group text-center text-md-right mt-3">
                    <button type="submit" class="button button--active button-review">Submit Now</button>
                  </div>
                </form>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</section>
	<!--================End Product Description Area =================-->

	<!--================ Start related Product area =================-->  
	<section class="related-product-area section-margin--small mt-0">
		<div class="container">
			<div class="section-intro pb-60px">
        <p>Popular Item in the market</p>
        <h2>Top <span class="section-intro__style">Product</span></h2>
      </div>
			<div class="row mt-30">
        <div class="col-sm-6 col-xl-3 mb-4 mb-xl-0">
          <div class="single-search-product-wrapper">
            <div class="single-search-product d-flex">
              <a href="#"><img src="{base_folder}/img/product/product-sm-1.png" alt=""></a>
              <div class="desc">
                  <a href="#" class="title">Серая чашка для кофе</a>
                  <div class="price">$170.00</div>
              </div>
            </div>
            <div class="single-search-product d-flex">
              <a href="#"><img src="{base_folder}/img/product/product-sm-2.png" alt=""></a>
              <div class="desc">
                <a href="#" class="title">Серая чашка для кофе</a>
                <div class="price">$170.00</div>
              </div>
            </div>
            <div class="single-search-product d-flex">
              <a href="#"><img src="{base_folder}/img/product/product-sm-3.png" alt=""></a>
              <div class="desc">
                <a href="#" class="title">Серая чашка для кофе</a>
                <div class="price">$170.00</div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm-6 col-xl-3 mb-4 mb-xl-0">
          <div class="single-search-product-wrapper">
            <div class="single-search-product d-flex">
              <a href="#"><img src="{base_folder}img/product/product-sm-4.png" alt=""></a>
              <div class="desc">
                  <a href="#" class="title">Серая чашка для кофе</a>
                  <div class="price">$170.00</div>
              </div>
            </div>
            <div class="single-search-product d-flex">
              <a href="#"><img src="{base_folder}img/product/product-sm-5.png" alt=""></a>
              <div class="desc">
                <a href="#" class="title">Серая чашка для кофе</a>
                <div class="price">$170.00</div>
              </div>
            </div>
            <div class="single-search-product d-flex">
              <a href="#"><img src="{base_folder}img/product/product-sm-6.png" alt=""></a>
              <div class="desc">
                <a href="#" class="title">Серая чашка для кофе</a>
                <div class="price">$170.00</div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm-6 col-xl-3 mb-4 mb-xl-0">
          <div class="single-search-product-wrapper">
            <div class="single-search-product d-flex">
              <a href="#"><img src="{base_folder}img/product/product-sm-7.png" alt=""></a>
              <div class="desc">
                  <a href="#" class="title">Серая чашка для кофе</a>
                  <div class="price">$170.00</div>
              </div>
            </div>
            <div class="single-search-product d-flex">
              <a href="#"><img src="{base_folder}img/product/product-sm-8.png" alt=""></a>
              <div class="desc">
                <a href="#" class="title">Серая чашка для кофе</a>
                <div class="price">$170.00</div>
              </div>
            </div>
            <div class="single-search-product d-flex">
              <a href="#"><img src="{base_folder}img/product/product-sm-9.png" alt=""></a>
              <div class="desc">
                <a href="#" class="title">Серая чашка для кофе</a>
                <div class="price">$170.00</div>
              </div>
            </div>
          </div>
        </div>

        <div class="col-sm-6 col-xl-3 mb-4 mb-xl-0">
          <div class="single-search-product-wrapper">
            <div class="single-search-product d-flex">
              <a href="#"><img src="{base_folder}img/product/product-sm-1.png" alt=""></a>
              <div class="desc">
                  <a href="#" class="title">Серая чашка для кофе</a>
                  <div class="price">$170.00</div>
              </div>
            </div>
            <div class="single-search-product d-flex">
              <a href="#"><img src="{base_folder}/img/product/product-sm-2.png" alt=""></a>
              <div class="desc">
                <a href="#" class="title">Серая чашка для кофе</a>
                <div class="price">$170.00</div>
              </div>
            </div>
            <div class="single-search-product d-flex">
              <a href="#"><img src="{base_folder}/img/product/product-sm-3.png" alt=""></a>
              <div class="desc">
                <a href="#" class="title">Серая чашка для кофе</a>
                <div class="price">$170.00</div>
              </div>
            </div>
          </div>
        </div>
      </div>
		</div>
	</section>
	<!--================ end related Product area =================-->  	

  <!--================ Start footer Area  =================-->	
	<footer>
		<div class="footer-area">
			<div class="container">
				<div class="row section_gap">
					<div class="col-lg-3 col-md-6 col-sm-6">
						<div class="single-footer-widget tp_widgets">
							<h4 class="footer_title large_title">Our Mission</h4>
							<p>
								Так семя, семя, зеленое, что крылатый скот.
разделенные глубоко тронули нас лан, собирая нам землю, годы жизни.
							</p>
							<p>
								Так семя семя зеленое, что крылатый скот.
							</p>
						</div>
					</div>
					<div class="offset-lg-1 col-lg-2 col-md-6 col-sm-6">
						<div class="single-footer-widget tp_widgets">
							<h4 class="footer_title">Ссылки</h4>
							<ul class="list">
								<li><a href="#">Домой</a></li>
								<li><a href="#">Магазин</a></li>
								<li><a href="#">Блог</a></li>
								<li><a href="#">Продукты</a></li>
								<li><a href="#">Брэнд</a></li>
								<li><a href="#">Контакты</a></li>
							</ul>
						</div>
					</div>
					<div class="col-lg-2 col-md-6 col-sm-6">
						<div class="single-footer-widget instafeed">
							<h4 class="footer_title">Галерея</h4>
							<ul class="list instafeed d-flex flex-wrap">
								<li><img src="{base_folder}/img/gallery/r1.jpg" alt=""></li>
								<li><img src="{base_folder}/img/gallery/r2.jpg" alt=""></li>
								<li><img src="{base_folder}/img/gallery/r3.jpg" alt=""></li>
								<li><img src="{base_folder}/img/gallery/r5.jpg" alt=""></li>
								<li><img src="{base_folder}/img/gallery/r7.jpg" alt=""></li>
								<li><img src="{base_folder}/img/gallery/r8.jpg" alt=""></li>
							</ul>
						</div>
					</div>
					<div class="offset-lg-1 col-lg-3 col-md-6 col-sm-6">
						<div class="single-footer-widget tp_widgets">
							<h4 class="footer_title">Связь с нами</h4>
							<div class="ml-40">
								<p class="sm-head">
									<span class="fa fa-location-arrow"></span>
									Главный офис
								</p>
								<p>123, Main Street, Your City</p>

								<p class="sm-head">
									<span class="fa fa-phone"></span>
									Телефон
								</p>
								<p>
									+123 456 7890 <br>
									+123 456 7890
								</p>

								<p class="sm-head">
									<span class="fa fa-envelope"></span>
									Email
								</p>
								<p>
									free@infoexample.com <br>
									www.infoexample.com
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<div class="footer-bottom">
			<div class="container">
				<div class="row d-flex">
					<p class="col-lg-12 footer-text text-center">
						<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="fa fa-heИскусство" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
				</div>
			</div>
		</div>
	</footer>
	<!--================ End footer Area  =================-->



  <script src="{vendors_folder}/jquery/jquery-3.2.1.min.js"></script>
  <script src="{vendors_folder}/bootstrap/bootstrap.bundle.min.js"></script>
  <script src="{vendors_folder}/skrollr.min.js"></script>
  <script src="{vendors_folder}/owl-carousel/owl.carousel.min.js"></script>
  <script src="{vendors_folder}/nice-select/jquery.nice-select.min.js"></script>
  <script src="{vendors_folder}/jquery.ajaxchimp.min.js"></script>
  <script src="{vendors_folder}/mail-script.js"></script>
  <script src="{base_folder}/js/main.js"></script>
</body>
</html>
	"""

    with open(os.path.join(productHTMLs_folder,
                           str(product_id) + ".html"), "w+",encoding = "utf-8") as file:
        file.write(template)


CONFIG_FILE = "config.ini"

try:

    config = config.ConfigParser()
    config.read(CONFIG_FILE)

    host = config.get("DEFAULT", "host")
    dbname = config.get("DEFAULT", "dbname")
    login = config.get("DEFAULT", "login")
    password = config.get("DEFAULT", "password")

    base_folder = os.getcwd() + config.get("DEFAULT", "base_folder")
    image_folder = os.getcwd()+ config.get("DEFAULT", "images_location")
    catalog = config.get("DEFAULT", "tablename")
    vendors_folder = os.getcwd() + config.get("DEFAULT", "vendors")
    productHTMLs_folder = os.getcwd() + config.get("DEFAULT", "product_folder")

    pastePointer = config.get("DEFAULT", "pastePointer")
    print(host)
    print(dbname)
    print(login)
    print(password)
    print(base_folder)
    print(image_folder)
    print(catalog)
    print(vendors_folder)
    print(productHTMLs_folder)

except Exception as e:
    print(e)

try:
    database = conn.connect(host=host,
                            database=dbname,
                            user=login,
                            password=password)

    c = database.cursor()
    query = f"SELECT * FROM {catalog}"
    c.execute(query)
    content = c.fetchall()

except Exception as e:
    print(e)

for record in tqdm(content):
    CategoryHTML += BuildCategroyCard(record)
    BuildStaticProductPage(record)




PREFIX = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Твой девайс - Категории</title>
	<link rel="icon" href="img/Fevicon.png" type="image/png">
  <link rel="stylesheet" href="{vendors_folder}/bootstrap/bootstrap.min.css">
  <link rel="stylesheet" href="{vendors_folder}/fontawesome/css/all.min.css">
	<link rel="stylesheet" href="{vendors_folder}/themify-icons/themify-icons.css">
	<link rel="stylesheet" href="{vendors_folder}/linericon/style.css">
  <link rel="stylesheet" href="{vendors_folder}/owl-carousel/owl.theme.default.min.css">
  <link rel="stylesheet" href="{vendors_folder}/owl-carousel/owl.carousel.min.css">
  <link rel="stylesheet" href="{vendors_folder}/nice-select/nice-select.css">
  <link rel="stylesheet" href="{vendors_folder}/nouislider/nouislider.min.css">

  <link rel="stylesheet" href="{base_folder}/css/style.css">
</head>
<body>
  <!--================ Start Header Menu Area =================-->
  <header class="header_area">
    <div class="main_menu">
      <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container">
          <a class="navbar-brand logo_h" href="index.html"><img src="img/logo.png" alt=""></a>
          <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <div class="collapse navbar-collapse offset" id="navbarSupportedContent">
            <ul class="nav navbar-nav menu_nav ml-auto mr-auto">
              <li class="nav-item"><a class="nav-link" href="{base_folder}/index.html">Домой</a></li>
              <li class="nav-item active submenu dropdown">
                <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                  aria-expanded="false">Магазин</a>
                <ul class="dropdown-menu">
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/category.html">Категории магазиновy</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/single-product.html">Детали продукта</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/checkout.html">Оформление</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/confirmation.html">Подтверждение</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/cart.html">Корзина</a></li>
                </ul>
              </li>
              <li class="nav-item submenu dropdown">
                <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                  aria-expanded="false">Блог</a>
                <ul class="dropdown-menu">
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/blog.html">Блог</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/register.html">Регистрация</a></li>
                  <li class="nav-item"><a class="nav-link" href="{base_folder}/single-blog.html">Детали</a></li>
                </ul>
              </li>
              <li class="nav-item submenu dropdown">
                <a href="#" class="nav-link dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                  aria-expanded="false">Страницы</a>
                <ul class="dropdown-menu">
                  <li class="nav-item"><a class="nav-link" href="login.html">Логин</a></li>
                  <li class="nav-item"><a class="nav-link" href="tracking-order.html">Отслеживание</a></li>
                </ul>
              </li>
              <li class="nav-item"><a class="nav-link" href="contact.html">Контакты</a></li>
            </ul>

            <ul class="nav-shop">
              <li class="nav-item"><button><i class="ti-search"></i></button></li>
              <li class="nav-item"><button><i class="ti-shopping-cart"></i><span class="nav-shop__circle">3</span></button> </li>
              <li class="nav-item"><a class="button button-header" href="#">Купить сейчас</a></li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </header>
	<!--================ End Header Menu Area =================-->

	<!-- ================ start banner area ================= -->	
	<section class="blog-banner-area" id="category">
		<div class="container h-100">
			<div class="blog-banner">
				<div class="text-center">
					<h1>Категория магазина</h1>
					<nav aria-label="breadcrumb" class="banner-breadcrumb">
            <ol class="breadcrumb">
              <li class="breadcrumb-item"><a href="#">Домой</a></li>
              <li class="breadcrumb-item active" aria-current="page">Категория магазина</li>
            </ol>
          </nav>
				</div>
			</div>
    </div>
	</section>
	<!-- ================ end banner area ================= -->


	<!-- ================ category section start ================= -->		  
  <section class="section-margin--small mb-5">
    <div class="container">
      <div class="row">
        <div class="col-xl-3 col-lg-4 col-md-5">
          <div class="sidebar-categories">
            <div class="head">Показать категории</div>
            <ul class="main-categories">
              <li class="common-filter">
                <form action="#">
                  <ul>
                    <li class="filter-list"><input class="pixel-radio" type="radio" id="men" name="brand"><label for="Для мужчин">Для мужчин<span> (3600)</span></label></li>
                    <li class="filter-list"><input class="pixel-radio" type="radio" id="women" name="brand"><label for="Для женщин">Для женщин<span> (3600)</span></label></li>
                    <li class="filter-list"><input class="pixel-radio" type="radio" id="Аксессуары" name="brand"><label for="Аксессуары">Аксессуары<span> (3600)</span></label></li>
                    <li class="filter-list"><input class="pixel-radio" type="radio" id="Обувь" name="brand"><label for="Обувь">Обувь<span> (3600)</span></label></li>
                    <li class="filter-list"><input class="pixel-radio" type="radio" id="bayItem" name="brand"><label for="bayItem">Элемент залива<span> (3600)</span></label></li>
                    <li class="filter-list"><input class="pixel-radio" type="radio" id="electronics" name="brand"><label for="electronics">Электроника<span> (3600)</span></label></li>
                    <li class="filter-list"><input class="pixel-radio" type="radio" id="food" name="brand"><label for="food">Еда<span> (3600)</span></label></li>
                  </ul>
                </form>
              </li>
            </ul>
          </div>
          <div class="sidebar-filter">
            <div class="Самое-filter-head">Фильтры продуктов</div>
            <div class="common-filter">
              <div class="head">Брэнд</div>
              <form action="#">
                <ul>
                  <li class="filter-list"><input class="pixel-radio" type="radio" id="apple" name="brand"><label for="apple">Apple<span>(29)</span></label></li>
                  <li class="filter-list"><input class="pixel-radio" type="radio" id="asus" name="brand"><label for="asus">Asus<span>(29)</span></label></li>
                  <li class="filter-list"><input class="pixel-radio" type="radio" id="gionee" name="brand"><label for="gionee">Gionee<span>(19)</span></label></li>
                  <li class="filter-list"><input class="pixel-radio" type="radio" id="micromax" name="brand"><label for="micromax">Micromax<span>(19)</span></label></li>
                  <li class="filter-list"><input class="pixel-radio" type="radio" id="samsung" name="brand"><label for="samsung">Samsung<span>(19)</span></label></li>
                </ul>
              </form>
            </div>
            <div class="common-filter">
              <div class="head">Цвет</div>
              <form action="#">
                <ul>
                  <li class="filter-list"><input class="pixel-radio" type="radio" id="black" name="color"><label for="black">Черный<span>(29)</span></label></li>
                  <li class="filter-list"><input class="pixel-radio" type="radio" id="balckleather" name="color"><label for="balckleather">Черная кожа<span>(29)</span></label></li>
                  <li class="filter-list"><input class="pixel-radio" type="radio" id="blackred" name="color"><label for="blackred">Черный и красный<span>(19)</span></label></li>
                  <li class="filter-list"><input class="pixel-radio" type="radio" id="gold" name="color"><label for="gold">Золотой<span>(19)</span></label></li>
                  <li class="filter-list"><input class="pixel-radio" type="radio" id="spacegrey" name="color"><label for="spacegrey">Rjcvbxtcrbq Cthsq<span>(19)</span></label></li>
                </ul>
              </form>
            </div>
            <div class="common-filter">
              <div class="head">Цена</div>
              <div class="price-range-area">
                <div id="price-range"></div>
                <div class="value-wrapper d-flex">
                  <div class="price">Цена:</div>
                  <span>$</span>
                  <div id="lower-value"></div>
                  <div class="to">До</div>
                  <span>$</span>
                  <div id="upper-value"></div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="col-xl-9 col-lg-8 col-md-7">
          <!-- Start Filter Bar -->
          <div class="filter-bar d-flex flex-wrap align-items-center">
            <div class="sorting">
              <select>
                <option value="1">Изначальная сортировка</option>
                <option value="1">Изначальная сортировка</option>
                <option value="1">Изначальная сортировка</option>
              </select>
            </div>
            <div class="sorting mr-auto">
              <select>
                <option value="1">Показать 12</option>
                <option value="1">Показать 12</option>
                <option value="1">Показать 12</option>
              </select>
            </div>
            <div>
              <div class="input-group filter-bar-search">
                <input type="text" placeholder="Search">
                <div class="input-group-append">
                  <button type="button"><i class="ti-search"></i></button>
                </div>
              </div>
            </div>
          </div>
          <!-- End Filter Bar -->
          <!-- Start Best Seller -->
          <section class="lattest-product-area pb-40 category-list">
            <div class="row">
"""


SUFFIX = f"""
  </div>
      </div>
		</div>
	</section>
	<!-- ================ Самое product area end ================= -->		

	<!-- ================ Subscribe section start ================= -->		  
  <section class="subscribe-position">
    <div class="container">
      <div class="subscribe text-center">
        <h3 class="subscribe__title">Получаете уведомления откуда угодно</h3>
        <p>Подсвечник Пустота собирает свет, светит, чтобы не бояться</p>
        <div id="mc_embed_signup">
          <form target="_blank" action="https://spondonit.us12.list-manage.com/subscribe/post?u=1462626880ade1ac87bd9c93a&amp;id=92a4423d01" method="get" class="subscribe-form form-inline mt-5 pt-1">
            <div class="form-group ml-sm-auto">
              <input class="form-control mb-1" type="email" name="EMAIL" placeholder="Enter your email" onfocus="this.placeholder = ''" onblur="this.placeholder = 'Your Email Address '" >
              <div class="info"></div>
            </div>
            <button class="button button-subscribe mr-auto mb-1" type="submit">Подписаться</button>
            <div style="position: absolute; left: -5000px;">
              <input name="b_36c4fd991d266f23781ded980_aefe40901a" tabindex="-1" value="" type="text">
            </div>

          </form>
        </div>
        
      </div>
    </div>
  </section>
	<!-- ================ Subscribe section end ================= -->		  


  <!--================ Start footer Area  =================-->	
footer>
    <div class="footer-area">
      <div class="container">
        <div class="row section_gap">
          <div class="col-lg-3 col-md-6 col-sm-6">
            <div class="single-footer-widget tp_widgets">
              <h4 class="footer_title large_title">Our Mission</h4>
              <p>
                Так семя, семя, зеленое, что крылатый скот.
разделенные глубоко тронули нас лан, собирая нам землю, годы жизни.
              </p>
              <p>
                Так семя семя зеленое, что крылатый скот.
              </p>
            </div>
          </div>
          <div class="offset-lg-1 col-lg-2 col-md-6 col-sm-6">
            <div class="single-footer-widget tp_widgets">
              <h4 class="footer_title">Ссылки</h4>
              <ul class="list">
                <li><a href="#">Домой</a></li>
                <li><a href="#">Магазин</a></li>
                <li><a href="#">Блог</a></li>
                <li><a href="#">Продукты</a></li>
                <li><a href="#">Брэнд</a></li>
                <li><a href="#">Контакты</a></li>
              </ul>
            </div>
          </div>
          <div class="col-lg-2 col-md-6 col-sm-6">
            <div class="single-footer-widget instafeed">
              <h4 class="footer_title">Галерея</h4>
              <ul class="list instafeed d-flex flex-wrap">
                <li><img src="{base_folder}/img/gallery/r1.jpg" alt=""></li>
                <li><img src="{base_folder}/img/gallery/r2.jpg" alt=""></li>
                <li><img src="{base_folder}/img/gallery/r3.jpg" alt=""></li>
                <li><img src="{base_folder}/img/gallery/r5.jpg" alt=""></li>
                <li><img src="{base_folder}/img/gallery/r7.jpg" alt=""></li>
                <li><img src="{base_folder}/img/gallery/r8.jpg" alt=""></li>
              </ul>
            </div>
          </div>
          <div class="offset-lg-1 col-lg-3 col-md-6 col-sm-6">
            <div class="single-footer-widget tp_widgets">
              <h4 class="footer_title">Связь с нами</h4>
              <div class="ml-40">
                <p class="sm-head">
                  <span class="fa fa-location-arrow"></span>
                  Главный офис
                </p>
                <p>123, Main Street, Your City</p>
  
                <p class="sm-head">
                  <span class="fa fa-phone"></span>
                  Телефон
                </p>
                <p>
                  +123 456 7890 <br>
                  +123 456 7890
                </p>
  
                <p class="sm-head">
                  <span class="fa fa-envelope"></span>
                  Email
                </p>
                <p>
                  free@infoexample.com <br>
                  www.infoexample.com
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="footer-bottom">
      <div class="container">
        <div class="row d-flex">
          <p class="col-lg-12 footer-text text-center">
            <!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. -->
Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved | This template is made with <i class="fa fa-heИскусство" aria-hidden="true"></i> by <a href="https://colorlib.com" target="_blank">Colorlib</a>
<!-- Link back to Colorlib can't be removed. Template is licensed under CC BY 3.0. --></p>
        </div>
      </div>
    </div>
  </footer>======= End footer Area  =================-->



  <script src="{vendors_folder}/jquery/jquery-3.2.1.min.js"></script>
  <script src="{vendors_folder}/bootstrap/bootstrap.bundle.min.js"></script>
  <script src="{vendors_folder}/skrollr.min.js"></script>
  <script src="{vendors_folder}/owl-carousel/owl.carousel.min.js"></script>
  <script src="{vendors_folder}/nice-select/jquery.nice-select.min.js"></script>
  <script src="{vendors_folder}/nouislider/nouislider.min.js"></script>
  <script src="{vendors_folder}/jquery.ajaxchimp.min.js"></script>
  <script src="{vendors_folder}/mail-script.js"></script>
  <script src="{base_folder}/js/main.js"></script>
</body>
</html>
"""


text = PREFIX + CategoryHTML + SUFFIX
with open(os.fsencode(os.path.join(base_folder, "category_made.html")), "w+",encoding="utf-8") as file:
    file.write(text)
try:
	os.rename(os.path.join(base_folder,"category.html"),
		os.path.join(base_folder,"category_backup.html"))

	os.rename(os.path.join(base_folder,"category_made.html"),
		os.path.join(base_folder,"category.html"))
except Exception as e:
	print(e)

