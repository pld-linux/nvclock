Summary:	nvidia overclock utility
Summary(pl):	narzêdzie do podkrêcania kart nvidia
Name:		nvclock
Version:	0.2
Release:	1
License:	GPL
Group:		Networking/Admin
Group(pl):	Sieciowe/Administracyjne
Source0:	ftp://ftp.evil3d.net/pub/Evil3D/nvclock/%{name}%{version}.tar.gz
URL:		http://www.evil3d.net/products/nvclock/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_bindir	%{_sbindir}

%description
This program allows you to overclock your nvidia card under linux.

%description -l pl
Ten program pozwala Ci na podkrêcanie Twojej karty graficznej NVidia pod
Linuxem.

%prep
%setup -q -n %{name}%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
gzip -9nf AUTHORS Change* NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
