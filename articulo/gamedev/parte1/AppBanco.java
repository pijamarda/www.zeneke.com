import java.util.Scanner;

class Banco
{
	class Cliente
	{
		Integer id;
		Integer saldo;
		String nombre;

		public Cliente(String nom, Integer cliente_id)
		{
			nombre = nom;		
			id = cliente_id;
			saldo = 0;
		}

		public boolean sacarDinero(Integer dinero)
		{
			if ((saldo - dinero) >= 0 )
			{
				saldo -= dinero;
				return true;
			}
			else return false;
		}

		public Integer ingresarDinero(Integer dinero)
		{
			if (dinero > 0)
				saldo += dinero;
			return saldo;
		}
		public Integer getId() {return id;}
		public Integer getSaldo() {return saldo;}
		public String getNombre() {return nombre;}
	}


	static Integer numClientes;
	Integer MAXCLIENTES;
	Cliente[] clientes;

	public Banco()
	{
		numClientes = 0;
		MAXCLIENTES = 1000;
		clientes = new Cliente[MAXCLIENTES];
	}

	public Integer menuPrincipal()
	{
		Integer opcion = -1;
		Scanner input = new Scanner(System.in);
		System.out.println("Bienvenido al Banco Lepton, seleccione una opcion");
		System.out.println("1. Crear cuenta");
		System.out.println("2. Sacar dinero");
		System.out.println("3. Ingresar dinero");
		System.out.println("0. Terminar aplicacion");
		opcion = input.nextInt();
		return opcion;
	}

	public void menuCrearCuenta()
	{
		String nombre = "";
		Scanner input = new Scanner(System.in);
		System.out.println("Ha elegido crear cuenta");
		System.out.println("Introduzca su nombre");		
		nombre = input.nextLine();
		System.out.println("Gracias "+nombre);
		crearCuenta(nombre);
	}

	private void crearCuenta(String nombre)
	{
		Integer numeroDeCliente = numClientes+1;
		clientes[numClientes] = new Cliente(nombre, numeroDeCliente);		
		System.out.println("Su numero de cliente es: "+ clientes[numClientes].getId());
		numClientes+=1;
	}

	public void sacarDinero()
	{
		String nombre = "";
		Scanner input = new Scanner(System.in);
		System.out.println("Ha elegido sacar dinero");
		System.out.println("Introduzca su id");		
		Integer id = input.nextInt();
		nombre = clientes[id-1].getNombre();
		System.out.println("Hola "+nombre+" ,cuanto desea sacar");
		Integer dinero = input.nextInt();
		if (clientes[id-1].sacarDinero(dinero))
			System.out.println("operacion aceptada");
		else
			System.out.println("operacion denegada");
		System.out.println("Su saldo es: "+ clientes[id-1].getSaldo());
	}

	public void ingresarDinero()
	{
		String nombre = "";
		Scanner input = new Scanner(System.in);
		System.out.println("Ha elegido ingresar dinero");
		System.out.println("Introduzca su id");		
		Integer id = input.nextInt();
		nombre = clientes[id-1].getNombre();
		System.out.println("Hola "+nombre+" ,cuanto desea ingresar");
		Integer dinero = input.nextInt();		
		System.out.println("Su saldo es: "+ clientes[id-1].ingresarDinero(dinero));
	}

}



public class AppBanco
{
	
	static Banco bancoLepton;

	public static void main(String args[])
	{
		Integer opcion = -5;

		bancoLepton = new Banco();
		while (opcion != 0)
		{
			opcion = bancoLepton.menuPrincipal();
			switch(opcion)
			{
				case 1: bancoLepton.menuCrearCuenta();
						break;
				case 2: bancoLepton.sacarDinero();
						break;
				case 3: bancoLepton.ingresarDinero();
						break;
				default: System.out.println("Opcion no encontrada");
			}
		}
	}	
}