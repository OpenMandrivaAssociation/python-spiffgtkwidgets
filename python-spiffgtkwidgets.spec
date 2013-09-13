%define git 59a713f

Summary:    Collection of useful Gtk widgets
Name:       python-spiffgtkwidgets
Version:    0.2.0
Release:    5.%{git}
            # src/SpiffGtkWidgets/FormEditor/Elements/Element.py
            # and src/SpiffGtkWidgets/FormEditor/FloatBox.py
            # are LGPLv3, all other AGPLv3
License:    AGPLv3 and LGPLv3
Group:      System/Libraries
URL:        https://github.com/knipknap/SpiffGtkWidgets
BuildArch:  noarch
Source0:    https://github.com/knipknap/SpiffGtkWidgets/tarball/%{git}
            # https://github.com/knipknap/SpiffGtkWidgets/issues/4
Patch0:     %{name}-fsf-fix.patch

Requires:   pygtk2.0
Requires:   python-hippo-canvas

BuildRequires: python-setuptools
BuildRequires: python-devel


%description
Spiff Gtk Widgets provides a collection of Gtk widgets
- An annotated text view and a calendar similar to Google's online calendar.


%prep
ln -sf %{SOURCE0} source0.tar.gz
%define SOURCE0 source0.tar.gz
%setup -q -n knipknap-SpiffGtkWidgets-%{git}
%patch0 -p1

%build
%{__python} setup.py --quiet build

%install
%{__python} setup.py --quiet install -O1 --skip-build --root %{buildroot}

%files
%doc AUTHORS COPYING ChangeLog README TODO
%{python_sitelib}/SpiffGtkWidgets
%{python_sitelib}/*.egg-info
