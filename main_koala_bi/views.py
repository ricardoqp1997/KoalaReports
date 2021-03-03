from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from login_koala_bi.models import CregevalUSer
from main_koala_bi.models import CompanyContent


# redireccionamiento de la pagina respecto a la autenticación del usuario
def index(request):
    if request.user.is_authenticated:
        return redirect('/main/informes')
    else:
        logout(request)
        return redirect('login/')


# Vista de la pagina principal del portal
@login_required(login_url='http://127.0.0.1:8000/login/')
def main(request):

    user_name = request.user.get_full_name()

    company_name = CompanyContent.objects.get(cliente_id=request.user.id).name

    company_logo = CompanyContent.objects.get(cliente_id=request.user.id).logo
    ##
    slide1_title = CompanyContent.objects.get(cliente_id=request.user.id).slide1_title
    slide1_contn = CompanyContent.objects.get(cliente_id=request.user.id).slide1_content
    slide1_imagn = CompanyContent.objects.get(cliente_id=request.user.id).slide1_img
    slide2_title = CompanyContent.objects.get(cliente_id=request.user.id).slide2_title
    slide2_contn = CompanyContent.objects.get(cliente_id=request.user.id).slide2_content
    slide2_imagn = CompanyContent.objects.get(cliente_id=request.user.id).slide2_img
    slide3_title = CompanyContent.objects.get(cliente_id=request.user.id).slide3_title
    slide3_contn = CompanyContent.objects.get(cliente_id=request.user.id).slide3_content
    slide3_imagn = CompanyContent.objects.get(cliente_id=request.user.id).slide3_img
    ##
    details_titl = CompanyContent.objects.get(cliente_id=request.user.id).details_maintitle
    details_deta = CompanyContent.objects.get(cliente_id=request.user.id).details_detail
    ##
    detail1_titl = CompanyContent.objects.get(cliente_id=request.user.id).detail1_title
    detail1_cont = CompanyContent.objects.get(cliente_id=request.user.id).detail1_content
    detail2_titl = CompanyContent.objects.get(cliente_id=request.user.id).detail2_title
    detail2_cont = CompanyContent.objects.get(cliente_id=request.user.id).detail2_content
    detail3_titl = CompanyContent.objects.get(cliente_id=request.user.id).detail3_title
    detail3_cont = CompanyContent.objects.get(cliente_id=request.user.id).detail3_content

    if request.user.is_authenticated:

        context_inicio = {
            'title': 'Informes Cregeval - Pagina principal',
            ##
            'user_name': user_name,
            'company_name': company_name,
            'company_logo': company_logo,
            ##
            'slide1_title': slide1_title,
            'slide1_contn': slide1_contn,
            'slide1_imagn': slide1_imagn,

            'slide2_title': slide2_title,
            'slide2_contn': slide2_contn,
            'slide2_imagn': slide2_imagn,

            'slide3_title': slide3_title,
            'slide3_contn': slide3_contn,
            'slide3_imagn': slide3_imagn,
            ##
            'details_titl': details_titl,
            'details_deta': details_deta,
            ##
            'detail1_titl': detail1_titl,
            'detail1_cont': detail1_cont,

            'detail2_titl': detail2_titl,
            'detail2_cont': detail2_cont,

            'detail3_titl': detail3_titl,
            'detail3_cont': detail3_cont,

        }
        return render(request, 'main.html', context_inicio)
    else:
        return redirect('/login/')


# Vista de la sección de informes del portal
@login_required(login_url='http://127.0.0.1:8000/login/')
def informes(request):

    company_bi = CompanyContent.objects.get(cliente_id=request.user.id).bi_link
    company_logo = CompanyContent.objects.get(cliente_id=request.user.id).logo
    company_name = CompanyContent.objects.get(cliente_id=request.user.id).name

    if request.user.is_authenticated:

        context_inicio = {
            'title': 'Informes Cregeval - Vista de informes',

            'company_logo': company_logo,
            ##
            'company_name': company_name,
            'informe_url': company_bi,
        }
        return render(request, 'informes.html', context_inicio)
    else:
        return redirect('/login/')
