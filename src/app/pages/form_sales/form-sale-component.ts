import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Input, Output } from '@angular/core';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import {Sale} from '../../../models/sales';

@Component({
  selector: 'app-form-sale',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './form-sale.component.html',
  styleUrl: './form-sale.component.css'
})
export class FormSaleComponent {
  public bt_title: string = "Guardar"
  public myForm: FormGroup

  // Guardar Venta
  @Output() saveSale = new EventEmitter<Sale>();
  // Recibir Venta a editar
  @Input() mySaleSelected: Sale | undefined;
  // Enviar Venta editada
  @Output() editSale = new EventEmitter<Sale>();

  constructor(private fb: FormBuilder) {
    this.myForm = this.fb.group({
      id: ['', [Validators.required, Validators.pattern("^[0-9]$")]],
      descripcion:['',[Validators.required, Validators.patter("^[a-zA-Z ]+$")]],
      id_titular: ['', [Validators.required, Validators.pattern("^[0-9]$")]],
      titular: ['', [Validators.required, Validators.pattern("^[a-zA-Z ]+$")]],
      monto: ['', [Validators.required, Validators.pattern("^[0-9]$")]],
      fecha: ['', [Validators.required]]
    });
  }

  get f() {
    return this.myForm.controls
  }

  onSubmit() {
    if (this.myForm.valid) {
      if (this.bt_title == "Actualizar") {
        this.editSale.emit(this.myForm.value as Sale)
        this.bt_title = "Guardar"
      }
      else {
        this.saveSale.emit(this.myForm.value as Sale)
      }
      this.myForm.reset()
    } else {
      console.log("Formulario no valido")
    }
  }

  ngOnChanges() {
    if (this.mySaleSelected) {
      this.myForm.patchValue({
        id: this.mySaleSelected.id,
        descripcion: this.mySaleSelected.descripcion,
        id_titular: this.mySaleSelected.id_titular,
        titular: this.mySaleSelected.titular,
        monto: this.mySaleSelected.monto,
        fecha: this.mySaleSelected.fecha
      });
      this.bt_title = "Actualizar"
    } else {
      this.bt_title = "Guardar"
    }
  }

  callCancel(){
    this.myForm.reset()
    this.bt_title = "Guardar"
  }

}
