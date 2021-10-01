from flask import Flask, request, session, Markup
from XL_3L import *

#Khai báo và khởi động ứng dụng
Ung_dung = Flask(__name__,static_url_path="Media", static_folder=".\\Media")
Ung_dung.secret_key = "123456789"
# Khai Báo biến toàn cục
Khung_HTML = Doc_Khung_HTML()
@Ung_dung.route('/',methods =['GET'])
def XL_Khoi_dong():
    Chuoi_HTML_Khung = Doc_Khung_HTML()
    Chuoi_HTML = Tao_Chuoi_HTML_Dang_nhap("NV_1", "NV_1", "")
    Chuoi_HTML = Chuoi_HTML_Khung.replace("Chuoi_HTML", Chuoi_HTML)
    return Chuoi_HTML

@Ung_dung.route('/Dang_nhap', methods = ['POST'])

def XL_Dang_nhap():

    Danh_Sach_Nhan_Vien = Doc_DS_NV()
    Chuoi_HTML_Khung = Doc_Khung_HTML()
    
    Danh_sach =[Nhan_vien for Nhan_vien in Danh_Sach_Nhan_Vien 
                             if Nhan_vien["Ten_Dang_nhap"] == request.form.get('Th_Ten_Dang_nhap') and 
                             Nhan_vien["Mat_khau"] ==request.form.get('Th_Mat_khau')]
    Hop_le = any(Danh_sach)
    if Hop_le :
            Nhan_vien = Danh_sach[0]
            session['Nhan_vien'] = Nhan_vien
            Danh_Sach_Nhan_Vien_Xem =[Nhan_vien]
            Chuoi_HTML = Tao_Chuoi_HTML_DS_NV(Danh_Sach_Nhan_Vien_Xem)
    else:
        Chuoi_HTML = Tao_Chuoi_HTML_Dang_nhap("", "", "Đăng nhập không hợp lệ")
    Chuoi_HTML = Chuoi_HTML_Khung.replace("Chuoi_HTML", Chuoi_HTML)
    return Chuoi_HTML

@Ung_dung.route('/Cap_nhat_Dien_thoai',methods =['POST'])

def XL_Cap_Nhat_Dien_Thoai() :
    Chuoi_HTML_Khung = Doc_Khung_HTML()
    Nhan_vien = session["Nhan_vien"]
    Dien_thoai = request.form.get("Th_Dien_thoai")
    Nhan_vien["Dien_thoai"] =Dien_thoai
    
    Ghi_Nhan_vien(Nhan_vien)
    Nhan_vien_xem = [Nhan_vien]
    session["Nhan_vien"] = Nhan_vien
    Chuoi_HTML = Tao_Chuoi_HTML_DS_NV(Nhan_vien_xem)
    Chuoi_HTML = Chuoi_HTML_Khung.replace("Chuoi_HTML", Chuoi_HTML)
    return Chuoi_HTML

    
@Ung_dung.route('/Cap_nhat_Dia_chi', methods = ['POST'])
def XL_Cap_nhat_Dia_chi():
    Chuoi_HTML_Khung = Doc_Khung_HTML()
    Nhan_vien = session["Nhan_vien"]
    Dia_chi = request.form.get("Th_Dia_chi")
    Nhan_vien["Dia_chi"] = Dia_chi
    Ghi_Nhan_vien(Nhan_vien)
    Nhan_vien_xem = [Nhan_vien]
    session["Nhan_vien"] = Nhan_vien
    Chuoi_HTML = Tao_Chuoi_HTML_DS_NV(Nhan_vien_xem)
    Chuoi_HTML = Chuoi_HTML_Khung.replace("Chuoi_HTML", Chuoi_HTML)
    return Chuoi_HTML

@Ung_dung.route('/Cap_nhat_Hinh', methods = ['POST'])
def XL_Cap_nhat_Hinh():
    Chuoi_HTML_Khung = Doc_Khung_HTML()
    Nhan_vien = session["Nhan_vien"]
    Hinh = request.files["Th_Hinh"]
    Ghi_Hinh_Nhan_vien(Nhan_vien, Hinh)
    Nhan_vien_xem = [Nhan_vien]
    session["Nhan_vien"] = Nhan_vien
    Chuoi_HTML = Tao_Chuoi_HTML_DS_NV(Nhan_vien_xem)
    Chuoi_HTML = Chuoi_HTML_Khung.replace("Chuoi_HTML", Chuoi_HTML)
    return Chuoi_HTML

@Ung_dung.route('/Nop_Don_xin_nghi', methods = ['POST'])
def XL_Nop_Don_xin_nghi():
    Chuoi_HTML_Khung = Doc_Khung_HTML()
    Nhan_vien = session["Nhan_vien"]
    Ngay_Bat_dau = request.form.get("Th_Ngay_Bat_dau")
    So_ngay = request.form.get("Th_So_ngay")
    Ly_do = request.form.get("Th_Ly_do")
    Nhan_vien = Tao_Don_Xin_nghi(Nhan_vien, Ngay_Bat_dau, So_ngay, Ly_do)
    Ghi_Nhan_vien(Nhan_vien)
    DS_NV_Xem = [Nhan_vien]
    session["Nhan_vien"] = Nhan_vien
    Chuoi_HTML = Tao_Chuoi_HTML_DS_NV(DS_NV_Xem)
    Chuoi_HTML = Chuoi_HTML_Khung.replace("Chuoi_HTML", Chuoi_HTML)
    return Chuoi_HTML
    
    

 
 