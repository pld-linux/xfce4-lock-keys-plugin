Summary:	Show status of lock key leds plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka panelu Xfce pokazująca status diod klawiatury
Name:		xfce4-lock-keys-plugin
Version:	1.0.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://ftp.pld-linux.org/people/baggins/XFCE/%{name}-%{version}.tar.bz2
# Source0-md5:	40680ac5871637fc86d52850ca763ab6
BuildRequires:	libxfce4ui-devel
BuildRequires:	libxfce4util-devel
BuildRequires:	xfce4-dev-tools >= 4.8.0
BuildRequires:	xfce4-panel-devel >= 4.8.0
Requires:	xfce4-panel >= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin shows the status of the CAPS-, NUM- and SCROLL-Lock keys
of your keyboard.

%description -l pl.UTF-8
Ta wtyczka pokazuje stan diod CAPS-, NUM- i SCROLL-Lock klawiatury.

%prep
%setup -q

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/panel-plugins/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun                                                                         
%update_icon_cache hicolor  

%files
%defattr(644,root,root,755)
%doc AUTHORS README THANKS
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/liblock-keys.so
%{_datadir}/xfce4/panel-plugins/lock-keys.desktop
%{_datadir}/xfce4/xfce4-lock-keys-plugin/*.png
%{_iconsdir}/hicolor/*/apps/xfce4-lock-keys-plugin.*
