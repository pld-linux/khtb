Summary:	GUI for htb.init script with XML data storage
Summary(pl.UTF-8):	Graficzny interfejs dla skryptu htb.init z danymi przechowywanymi w XML-u
Name:		khtb
Version:	0.2
Release:	1
License:	GPL
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/khtb/%{name}-%{version}.tar.gz
# Source0-md5:	ff1ed8611dd82347922f07028d03f6ad
URL:		http://sourceforge.net/projects/khtb/
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KHtb is a GUI for htb.init script with XML data storage. It can
import-export htb.init tree. Can be used to edit remote htb.init tree
(in the future).

%description -l pl.UTF-8
KHtb to graficzny interfejs użytkownika do skryptu htb.init z
przechowywaniem danych w formacie XML. Potrafi importować i
eksportować drzewo htb.init. Może być używany do modyfikowania
zdalnych drzew htb.init (w przyszłości).

%prep
%setup -q

echo 'Categories=Qt;KDE;Network;' >> src/khtb.desktop

%build
export kde_htmldir=%{_kdedocdir}
%configure

%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	shelldesktopdir=%{_desktopdir}

%find_lang khtb --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/apps/khtb
%{_iconsdir}/*/*/apps/*.png
%{_desktopdir}/*.desktop
