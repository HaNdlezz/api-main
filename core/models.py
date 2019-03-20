from __future__ import unicode_literals
from django.shortcuts import get_object_or_404
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from datetime import date

class alumno(models.Model):
	rut = models.CharField(max_length=250,null=True,blank=True)
	nombre = models.CharField(max_length=250,null=True,blank=True)
	fecha_nacimiento = models.CharField(max_length=250,null=True,blank=True)
	campus = models.CharField(max_length=250,null=True,blank=True)
	unidad_academica = models.CharField(max_length=250,null=True,blank=True)
	programa = models.CharField(max_length=250,null=True,blank=True)
	carrera = models.CharField(max_length=250,null=True,blank=True)
	especialidad = models.CharField(max_length=250,null=True,blank=True)
	mencion = models.CharField(max_length=250,null=True,blank=True)
	estado = models.CharField(max_length=250,null=True,blank=True)
	matriculado = models.CharField(max_length=250,null=True,blank=True)
	bloqueo_sin_matricula = models.CharField(max_length=250,null=True,blank=True)
	retencion_financiera = models.CharField(max_length=250,null=True,blank=True)
	periodo_ultima_actualizacion = models.CharField(max_length=250,null=True,blank=True)
	periodo_ctgl = models.CharField(max_length=250,null=True,blank=True)
	periodo_admision = models.CharField(max_length=250,null=True,blank=True)
	tipo_alumno = models.CharField(max_length=250,null=True,blank=True)
	ppa = models.CharField(max_length=250,null=True,blank=True)
	pga_programa = models.CharField(max_length=250,null=True,blank=True)
	pga_historico = models.CharField(max_length=250,null=True,blank=True)
	asignaturas_aprobadas = models.CharField(max_length=250,null=True,blank=True)
	creditos_aprobados_programa = models.CharField(max_length=250,null=True,blank=True)
	via_titulacion = models.CharField(max_length=250,null=True,blank=True)
	domicilio = models.CharField(max_length=250,null=True,blank=True)
	fono_celular = models.CharField(max_length=250,null=True,blank=True)
	fono_particular = models.CharField(max_length=250,null=True,blank=True)
	correo_unab = models.CharField(max_length=250,null=True,blank=True)
	correo_personal = models.CharField(max_length=250,null=True,blank=True)
	
	def __str__(self):
		return self.rut + " - " + self.nombre + " - " + self.carrera
		
class docente(models.Model):
	nombre = models.CharField(max_length=250,null=True,blank=True)
	mail = models.CharField(max_length=250,null=True,blank=True)
	run = models.CharField(max_length=250,null=True,blank=True)
	titulo = models.CharField(max_length=250,null=True,blank=True)
	grado = models.CharField(max_length=250,null=True,blank=True)
	jornada = models.CharField(max_length=250,null=True,blank=True)
	sede = models.CharField(max_length=250,null=True,blank=True)
	asignatura = models.CharField(max_length=250,null=True,blank=True)
	ano = models.CharField(max_length=250,null=True,blank=True)
	semestre = models.CharField(max_length=250,null=True,blank=True)
	opa1 = models.CharField(max_length=250,null=True,blank=True)
	opa2 = models.CharField(max_length=250,null=True,blank=True)
	opa3 = models.CharField(max_length=250,null=True,blank=True)
	opa4 = models.CharField(max_length=250,null=True,blank=True)
	opa5 = models.CharField(max_length=250,null=True,blank=True)
	opb1 = models.CharField(max_length=250,null=True,blank=True)
	opb2 = models.CharField(max_length=250,null=True,blank=True)
	opb3 = models.CharField(max_length=250,null=True,blank=True)
	opb4 = models.CharField(max_length=250,null=True,blank=True)
	opb5 = models.CharField(max_length=250,null=True,blank=True)
	opc1 = models.CharField(max_length=250,null=True,blank=True)
	opc2 = models.CharField(max_length=250,null=True,blank=True)
	opc3 = models.CharField(max_length=250,null=True,blank=True)
	opc4 = models.CharField(max_length=250,null=True,blank=True)
	opc5 = models.CharField(max_length=250,null=True,blank=True)
	opd1 = models.CharField(max_length=250,null=True,blank=True)
	opd2 = models.CharField(max_length=250,null=True,blank=True)
	opd3 = models.CharField(max_length=250,null=True,blank=True)
	opd4 = models.CharField(max_length=250,null=True,blank=True)
	opd5 = models.CharField(max_length=250,null=True,blank=True)
	ope1 = models.CharField(max_length=250,null=True,blank=True)
	ope2 = models.CharField(max_length=250,null=True,blank=True)
	ope3 = models.CharField(max_length=250,null=True,blank=True)
	ope4 = models.CharField(max_length=250,null=True,blank=True)
	ope5 = models.CharField(max_length=250,null=True,blank=True)
	opf1 = models.CharField(max_length=250,null=True,blank=True)
	opf2 = models.CharField(max_length=250,null=True,blank=True)
	opf3 = models.CharField(max_length=250,null=True,blank=True)
	opf4 = models.CharField(max_length=250,null=True,blank=True)
	opf5 = models.CharField(max_length=250,null=True,blank=True)
	opg1 = models.CharField(max_length=250,null=True,blank=True)
	opg2 = models.CharField(max_length=250,null=True,blank=True)
	opg3 = models.CharField(max_length=250,null=True,blank=True)
	opg4 = models.CharField(max_length=250,null=True,blank=True)
	opg5 = models.CharField(max_length=250,null=True,blank=True)
	oph1 = models.CharField(max_length=250,null=True,blank=True)
	oph2 = models.CharField(max_length=250,null=True,blank=True)
	oph3 = models.CharField(max_length=250,null=True,blank=True)
	oph4 = models.CharField(max_length=250,null=True,blank=True)
	oph5 = models.CharField(max_length=250,null=True,blank=True)
	opi1 = models.CharField(max_length=250,null=True,blank=True)
	opi2 = models.CharField(max_length=250,null=True,blank=True)
	opi3 = models.CharField(max_length=250,null=True,blank=True)
	opi4 = models.CharField(max_length=250,null=True,blank=True)
	opi5 = models.CharField(max_length=250,null=True,blank=True)
	opj1 = models.CharField(max_length=250,null=True,blank=True)
	opj2 = models.CharField(max_length=250,null=True,blank=True)
	opj3 = models.CharField(max_length=250,null=True,blank=True)
	opj4 = models.CharField(max_length=250,null=True,blank=True)
	opj5 = models.CharField(max_length=250,null=True,blank=True)
	opk1 = models.CharField(max_length=250,null=True,blank=True)
	opk2 = models.CharField(max_length=250,null=True,blank=True)
	opk3 = models.CharField(max_length=250,null=True,blank=True)
	opk4 = models.CharField(max_length=250,null=True,blank=True)
	opk5 = models.CharField(max_length=250,null=True,blank=True)
	va1 = models.CharField(max_length=250,null=True,blank=True)
	va2 = models.CharField(max_length=250,null=True,blank=True)
	va3 = models.CharField(max_length=250,null=True,blank=True)
	va4 = models.CharField(max_length=250,null=True,blank=True)
	va5 = models.CharField(max_length=250,null=True,blank=True)
	va5 = models.CharField(max_length=250,null=True,blank=True)
	vpb1 = models.CharField(max_length=250,null=True,blank=True)
	vpb2 = models.CharField(max_length=250,null=True,blank=True)
	vpb3 = models.CharField(max_length=250,null=True,blank=True)
	vpb4 = models.CharField(max_length=250,null=True,blank=True)
	vpb5 = models.CharField(max_length=250,null=True,blank=True)
	vpc1 = models.CharField(max_length=250,null=True,blank=True)
	vpc2 = models.CharField(max_length=250,null=True,blank=True)
	vpc3 = models.CharField(max_length=250,null=True,blank=True)
	vpc4 = models.CharField(max_length=250,null=True,blank=True)
	vpc5 = models.CharField(max_length=250,null=True,blank=True)
	vpd1 = models.CharField(max_length=250,null=True,blank=True)
	vpd2 = models.CharField(max_length=250,null=True,blank=True)
	vpd3 = models.CharField(max_length=250,null=True,blank=True)
	vpd4 = models.CharField(max_length=250,null=True,blank=True)
	vpd5 = models.CharField(max_length=250,null=True,blank=True)
	ea1 = models.CharField(max_length=250,null=True,blank=True)
	ea2 = models.CharField(max_length=250,null=True,blank=True)
	ea3 = models.CharField(max_length=250,null=True,blank=True)
	ea4 = models.CharField(max_length=250,null=True,blank=True)
	ea5 = models.CharField(max_length=250,null=True,blank=True)
	eb1 = models.CharField(max_length=250,null=True,blank=True)
	eb2 = models.CharField(max_length=250,null=True,blank=True)
	eb3 = models.CharField(max_length=250,null=True,blank=True)
	eb4 = models.CharField(max_length=250,null=True,blank=True)
	eb5 = models.CharField(max_length=250,null=True,blank=True)
	ec1 = models.CharField(max_length=250,null=True,blank=True)
	ec2 = models.CharField(max_length=250,null=True,blank=True)
	ec3 = models.CharField(max_length=250,null=True,blank=True)
	ec4 = models.CharField(max_length=250,null=True,blank=True)
	ec5 = models.CharField(max_length=250,null=True,blank=True)
	ed1 = models.CharField(max_length=250,null=True,blank=True)
	ed2 = models.CharField(max_length=250,null=True,blank=True)
	ed3 = models.CharField(max_length=250,null=True,blank=True)
	ed4 = models.CharField(max_length=250,null=True,blank=True)
	ed5 = models.CharField(max_length=250,null=True,blank=True)
	ee1 = models.CharField(max_length=250,null=True,blank=True)
	ee2 = models.CharField(max_length=250,null=True,blank=True)
	ee3 = models.CharField(max_length=250,null=True,blank=True)
	ee4 = models.CharField(max_length=250,null=True,blank=True)
	ee5 = models.CharField(max_length=250,null=True,blank=True)
	ef1 = models.CharField(max_length=250,null=True,blank=True)
	ef2 = models.CharField(max_length=250,null=True,blank=True)
	ef3 = models.CharField(max_length=250,null=True,blank=True)
	ef4 = models.CharField(max_length=250,null=True,blank=True)
	ef5 = models.CharField(max_length=250,null=True,blank=True)
	eg1 = models.CharField(max_length=250,null=True,blank=True)
	eg2 = models.CharField(max_length=250,null=True,blank=True)
	eg3 = models.CharField(max_length=250,null=True,blank=True)
	eg4 = models.CharField(max_length=250,null=True,blank=True)
	eg5 = models.CharField(max_length=250,null=True,blank=True)
	opn1 = models.CharField(max_length=250,null=True,blank=True)
	opn2 = models.CharField(max_length=250,null=True,blank=True)
	opn3 = models.CharField(max_length=250,null=True,blank=True)
	opn4 = models.CharField(max_length=250,null=True,blank=True)
	opn5 = models.CharField(max_length=250,null=True,blank=True)
	vn1 = models.CharField(max_length=250,null=True,blank=True)
	vn2 = models.CharField(max_length=250,null=True,blank=True)
	vn3 = models.CharField(max_length=250,null=True,blank=True)
	vn4 = models.CharField(max_length=250,null=True,blank=True)
	vn5 = models.CharField(max_length=250,null=True,blank=True)
	es1 = models.CharField(max_length=250,null=True,blank=True)
	es2 = models.CharField(max_length=250,null=True,blank=True)
	es3 = models.CharField(max_length=250,null=True,blank=True)
	es4 = models.CharField(max_length=250,null=True,blank=True)
	es5 = models.CharField(max_length=250,null=True,blank=True)
	nivel1 = models.CharField(max_length=250,null=True,blank=True)
	nivel2 = models.CharField(max_length=250,null=True,blank=True)
	nivel3 = models.CharField(max_length=250,null=True,blank=True)
	nivel4 = models.CharField(max_length=250,null=True,blank=True)
	nivel5 = models.CharField(max_length=250,null=True,blank=True)
	evaluacion = models.CharField(max_length=250,null=True,blank=True)

	def __str__(self):
		return self.run + " - " + self.nombre + " - " + self.asignatura + " - " + self.sede + " - " + self.ano + "-" + self.jornada